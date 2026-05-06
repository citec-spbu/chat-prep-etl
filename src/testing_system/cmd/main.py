import asyncio
import sys
import logging
import logging.config
import yaml
#from aiohttp import web
from testing_system.internal.adapter.assistants.ollama import OllamaAssistant
from testing_system.internal.adapter.assistants.mock import MockAssistant
from testing_system.internal.adapter.retrievers.mock import MockRetriever
from testing_system.internal.controller.Orchestrator import Orchestrator
from testing_system.internal.domain.value_objects import RetrievedDocument

async def main():
    try:
        config_path = sys.argv[1] #Usage: python -m testing_system.cmd.main <config.yaml>
    except:
        config_path = "testing_system/config/config.yaml"
    with open(config_path, 'r') as f:
        cfg = yaml.safe_load(f)

    logging.config.dictConfig(cfg.get("logging", {}))
    logger = logging.getLogger(__name__)
    logger.info("Starting Testing System")
    orchestrator = Orchestrator(cfg["testing_system"]) #TODO
    await orchestrator.execute_experiments(cfg["testing_system"]["loaders"]["path"])
    '''
    server_port = cfg.get("testing_system", {}).get("port", 2222)
    logger.info("HTTP server listening on port %d", server_port)
    web.run_app(app, port=server_port)
    '''
    print("Done")
    print(orchestrator.runner.registry.select(None))

if __name__ == "__main__":
    asyncio.run(main())