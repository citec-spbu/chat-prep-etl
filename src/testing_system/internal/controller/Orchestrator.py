import copy
import logging

from testing_system.internal.adapter.assistants.API import OpenAIAssistant
from testing_system.internal.adapter.assistants.mock import MockAssistant
from testing_system.internal.adapter.assistants.ollama import OllamaAssistant
from testing_system.internal.adapter.config.yaml_experiment_loader import YamlExperimentLoader
from testing_system.internal.adapter.registries.local import LocalRegistry
from testing_system.internal.adapter.registries.mock import MockRegistry
from testing_system.internal.adapter.retrievers.etl import EtlRetriever
from testing_system.internal.adapter.retrievers.mock import MockRetriever
from testing_system.internal.domain.interfaces import IAssistant, IExperimentLoader, IRegistry, IRetriever
from testing_system.internal.usecase.Eval import Eval
from testing_system.internal.usecase.Runner import Runner
from testing_system.internal.usecase.Loader import Loader 

logger = logging.getLogger(__name__)

class Orchestrator:
    """
    Initializes all the adapters and usecases
    Loads every experiment from directory
    Provides every Experiment with Runner
    Saves the results
    """
    def __init__(self, cfg: dict):
        self.assistant = self._choose_assistant(cfg["assistants"])
        self.retrievers = self._choose_retriever(cfg["retrievers"])
        self.registry = self._choose_registry(cfg["registries"])
        loader = self._choose_loader(cfg["loaders"])
        logger.info("Orchestrator: Adapters are initialized successfully"+
            f"""\n"Orchestrator: init Assistant: {type(self.assistant)}"""+
            f"""\n"Orchestrator: init Retrievers: {type(self.retrievers[0])}"""+
            f"""\n"Orchestrator: init Registry: {type(self.registry)}"""+
            f"""\n"Orchestrator: init Loader: {type(loader)}"""
        )
        self.eval=Eval(**cfg["eval"])
        self.raw_runner = Runner(
            registry=self.registry,
            assistant=self.assistant,
            retriever=self.retrievers[0],
            eval=self.eval,
            num_process_workers=cfg["num_process_workers"],
            num_eval_workers=cfg["num_eval_workers"]
        )
        self.clean_runner = Runner(
            registry=self.registry,
            assistant=self.assistant,
            retriever=self.retrievers[1],
            eval=self.eval,
            num_process_workers=cfg["num_process_workers"],
            num_eval_workers=cfg["num_eval_workers"]
        )
        self.loader = Loader(
            loader = loader
        )
        self.progress = {"total": 0, "completed": 0}

    async def execute_experiments(self, path: str):
        experiments_raw = self.loader.execute(path)
        experiments_clean = copy.deepcopy(experiments_raw)
        self.progress = {"total": 2*len(experiments_raw), "completed": 0}

        for experiment in experiments_raw:
            experiment = await self.raw_runner.run(experiment)
            logger.info(f"Orchestrator: Experiment raw '{experiment.id}:{experiment.name}' is complete in {experiment.finished_at}")
            self.progress["completed"] += 1

        for experiment in experiments_clean:
            experiment = await self.clean_runner.run(experiment)
            logger.info(f"Orchestrator: Experiment clean '{experiment.id}:{experiment.name}' is complete in {experiment.finished_at}")
            self.progress["completed"] += 1

    def show_experiments(self):
        return self.registry.select()

    def _choose_assistant(self, cfg: dict) -> IAssistant:
        if cfg["type"] == "ollama":
            return OllamaAssistant(
                model=cfg["ollama"]["model"], 
                base_url=f"http://{cfg['ollama']['host']}:{cfg['ollama']['port']}"
                )
        elif cfg["type"] == "cloud":
            return OpenAIAssistant(
                model=cfg["cloud"]["model"], 
                base_url=cfg["cloud"]["base_url"],
                temperature=cfg["cloud"]["temperature"]
                )
        else:
            return MockAssistant()
        
    def _choose_retriever(self, cfg: dict) -> IRetriever:
        if cfg["type"] == "etl_service":
            return (
                EtlRetriever(
                    url = f"http://{cfg["etl_service"]["host"]}:{cfg["etl_service"]["port"]}",
                    chat_id = cfg["etl_service"]["chat_id"],
                    k = cfg["etl_service"]["k"],
                    clean="raw"
                ),
                EtlRetriever(
                    url = f"http://{cfg["etl_service"]["host"]}:{cfg["etl_service"]["port"]}",
                    chat_id = cfg["etl_service"]["chat_id"],
                    k = cfg["etl_service"]["k"],
                    clean="clean"
                )
            )
        else:
            return (MockRetriever("raw"),MockRetriever("clean"))

    def _choose_registry(self, cfg: dict) -> IRegistry:
        if cfg["type"] == "postgres":
            raise NotImplementedError
        elif cfg["type"] == "local":
            return LocalRegistry(cfg["local"]["path"])
        else:
            return MockRegistry()
        
    def _choose_loader(self, cfg: dict) -> IExperimentLoader:
        if cfg["type"] == "yaml":
            return YamlExperimentLoader()
        else:
            raise NotImplementedError
        