import asyncio
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import logging
from typing import Any, Dict, List, Optional
from datetime import datetime, timezone

from testing_system.internal.domain.entities import Answer, Experiment, MetricValue, Question
from testing_system.internal.domain.interfaces import \
    IAssistant, IRetriever, IRegistry
from testing_system.internal.usecase.Eval import Eval
from testing_system.internal.usecase.ProcessQuery import Processor

logger = logging.getLogger(__name__)

class Runner:
    """Main testing pipeline"""
    def __init__(self, 
                 registry: IRegistry,
                 assistant: IAssistant, 
                 retriever: IRetriever,
                 eval: Eval,
                 num_process_workers: int = 1,
                 num_eval_workers: int = 1,
                 ):
        self.registry = registry
        self.processor = Processor(assistant, retriever)
        self.eval = eval
        #   for asyncio
        self.num_process_workers = num_process_workers
        self.num_eval_workers = num_eval_workers

        self.process_queue = asyncio.Queue()
        self.eval_queue = asyncio.Queue()
    
    def _exist(self, experiment: Experiment) -> Experiment:
        """Checks the existence of the configuration in Registry"""
        return self.registry.check(experiment=experiment)
    
    def _save(self, experiment: Experiment):
        """Saves the experiment via registry"""
        self.registry.push(experiment=experiment)
        return

    def _run_process(self, q: Question) -> Answer:
        response = self.processor.execute(
            question = q.text, 
            system_prompt = q.metadata.get("system_prompt", None),
            temperature = q.metadata.get("temperature", None),
            metadata=None
        )
        return Answer(
            id = q.id,
            text = response.answer,
            retrieved_context=response.retrieved_context,
            token_count=response.token_count,
            latency_ms=response.latency_ms,
            metadata=None
        )
    
    def _run_eval(self, q: Question, a: Answer) -> List[MetricValue]:
        return self.eval.execute(q, a)

    async def _process_worker(self, executor):
        while True:
            query = await self.process_queue.get()
            try:
                loop = asyncio.get_running_loop()
                processed = await loop.run_in_executor(executor, self._run_process, query)
                await self.eval_queue.put((query,processed))
            except Exception as e:
                logger.error(f"Processor: Process failed for exp {query.id}: {e}")
            finally:
                self.process_queue.task_done()
    
    async def _eval_worker(self, executor):
        while True:
            q,a = await self.eval_queue.get()
            try:
                loop = asyncio.get_running_loop()
                evaluated = await loop.run_in_executor(executor, self._run_eval, q, a)
                logger.info(f"Processor: Query {q.id} completed")
                self.experiment.add(a,evaluated)
            except Exception as e:
                logger.error(f"Processor: Eval failed for query {q.id}: {e}")
            finally:
                self.eval_queue.task_done()

    async def run(self,experiment: Experiment) -> Experiment:
        """
        Main for Runner
        input: Experiment
        output: Experiment
        For every Experiment checks the existence in registry (TODO),
        runs only unseen configurations.
        Processing every single query, evaluates 

        Usage example:
        runner = Runner(...,
                num_process_workers=1,
                num_eval_workers=1,
                use_threads=True) 
        await runner.run(experiment)
        """
        
        experiment_from_registry = self._exist(experiment=experiment)
        if experiment_from_registry != None:
            logger.info(f"Processor: found {experiment_from_registry.id} Experiment in registry")
            return experiment_from_registry
        self.experiment = experiment

        #start_time
        self.experiment.started_at = datetime.now(timezone.utc)
        

        for q in self.experiment.questions:
            await self.process_queue.put(q)

        max_workers = max(self.num_process_workers, self.num_eval_workers)
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            process_tasks = [
                asyncio.create_task(self._process_worker(executor))
                for _ in range(self.num_process_workers)
            ]
            eval_tasks = [
                asyncio.create_task(self._eval_worker(executor))
                for _ in range(self.num_eval_workers)
            ]

            await self.process_queue.join()
            await self.eval_queue.join()

            for task in process_tasks + eval_tasks:
                task.cancel()
            await asyncio.gather(*process_tasks, *eval_tasks, return_exceptions=True)

        #end_time
        self.experiment.finished_at = datetime.now(timezone.utc)
        self._save(experiment=self.experiment)
        return self.experiment
