import logging

from testing_system.internal.adapter.assistants.mock import MockAssistant
from testing_system.internal.adapter.assistants.ollama import OllamaAssistant
from testing_system.internal.adapter.config.yaml_experiment_loader import YamlExperimentLoader
from testing_system.internal.adapter.registries.local import LocalRegistry
from testing_system.internal.adapter.registries.mock import MockRegistry
from testing_system.internal.adapter.retrievers.mock import MockRetriever
from testing_system.internal.domain.interfaces import IAssistant, IExperimentLoader, IRegistry, IRetriever
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
        assistant = self._choose_assistant(cfg["assistants"])
        retriever = self._choose_retriever(cfg["retrievers"])
        registry = self._choose_registry(cfg["registries"])
        loader = self._choose_loader(cfg["loaders"])
        logger.info("Orchestrator: Adapters are initialized successfully")
        logger.info(
            f"""Orchestrator: init Assistant: {type(assistant)}\n"""+
            f"""Orchestrator: init Retriever: {type(retriever)}\n"""+
            f"""Orchestrator: init Registry: {type(registry)}\n"""+
            f"""Orchestrator: init Loader: {type(loader)}\n"""
            )
        self.runner = Runner(
            registry=registry,
            assistant=assistant,
            retriever=retriever,
            num_process_workers=cfg["num_process_workers"],
            num_eval_workers=cfg["num_eval_workers"]
        )
        self.loader = Loader(
            loader = loader
        )

    async def execute_experiments(self, path: str):
        experiments = self.loader.execute(path)
        for experiment in experiments:
            experiment = await self.runner.run(experiment)
            logger.info(f"Orchestrator: Experiment '{experiment.id}:{experiment.name}' is complete in {experiment.finished_at}")


    def _choose_assistant(self, cfg: dict) -> IAssistant:
        if cfg["type"] == "ollama":
            return OllamaAssistant(
                model=cfg["ollama"]["model"], 
                base_url=f"http://{cfg['ollama']['host']}:{cfg['ollama']['port']}"
                )
        elif cfg["type"] == "cloud":
            raise NotImplementedError
            return OpenAIAssistant(
                model=cfg["cloud"]["model"], 
                base_url=cfg["cloud"]["base_url"],
                temperature=cfg["cloud"]["temperature"]
                )
        else:
            return MockAssistant()
        
    def _choose_retriever(self, cfg: dict) -> IRetriever:
        if cfg["type"] == "etl_service":
            raise NotImplementedError
        else:
            return MockRetriever()

    def _choose_registry(self, cfg: dict) -> IRegistry:
        if cfg["type"] == "postgres":
            raise NotImplementedError
        if cfg["type"] == "local":
            return LocalRegistry(cfg["local"]["path"])
        else:
            return MockRegistry()
        
    def _choose_loader(self, cfg: dict) -> IExperimentLoader:
        if cfg["type"] == "yaml":
            return YamlExperimentLoader()
        else:
            raise NotImplementedError
        