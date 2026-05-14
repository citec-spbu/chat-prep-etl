import asyncio
import sys
import logging
import logging.config
import yaml
from testing_system.internal.controller.Orchestrator import Orchestrator

async def main():
    try:
        config_path = sys.argv[1] #Usage: python -m testing_system.cmd.main <config.yaml>
    except IndexError:
        config_path = "testing_system/config/config.yaml"
    try:
        with open(config_path, 'r') as f:
            cfg = yaml.safe_load(f)
    except FileNotFoundError:
        logger.error(f"Config file not found: {config_path}")
        sys.exit(1)
    except yaml.YAMLError as e:
        logger.error(f"Failed to parse config file: {e}")
        sys.exit(1)

    logging.config.dictConfig(cfg.get("logging", {}))
    logger = logging.getLogger(__name__)
    logger.info("Starting Testing System")
    logger.info(f"Evaluation is provided by {cfg["testing_system"]["eval"]}")
    orchestrator = Orchestrator(cfg["testing_system"])
    await orchestrator.execute_experiments(cfg["testing_system"]["loaders"]["path"])
    '''
    server_port = cfg.get("testing_system", {}).get("port", 2222)
    logger.info("HTTP server listening on port %d", server_port)
    web.run_app(app, port=server_port)
    '''
    logger.debug("Done")
    logger.debug(f"Registry state: {orchestrator.runner.registry.select(None)}")

if __name__ == "__main__":
    asyncio.run(main())