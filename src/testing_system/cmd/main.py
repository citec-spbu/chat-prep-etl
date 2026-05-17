import asyncio
import sys
import logging
import logging.config
import yaml
import sys
sys.path.append('/workspace/chat-prep-etl/src')
from testing_system.internal.controller.Orchestrator import Orchestrator
import uvicorn

from testing_system.internal.controller.server import create_app

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
    logger.info(f"Evaluation is provided by {cfg['testing_system']['eval']}")
    orchestrator = Orchestrator(cfg["testing_system"])

    app = create_app(orchestrator=orchestrator, config=cfg, logger=logger)
    config = uvicorn.Config(
        app,
        host=cfg["testing_system"]["host"],
        port=cfg["testing_system"]["port"],
        log_config=cfg.get("logging", {}),
    )
    server = uvicorn.Server(config)
    await server.serve()

    return await orchestrator.execute_experiments("/workspace/chat-prep-etl/experiments")
if __name__ == "__main__":
    asyncio.run(main())