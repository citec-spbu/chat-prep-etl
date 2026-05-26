import asyncio
import os
import sys
import logging
import logging.config
import yaml
import sys
from src.etl.presentation.api import create_app
import uvicorn

async def main():
    try:
        config_path = sys.argv[1] #Usage: python etl.cmd.main <config.yaml>
    except IndexError:
        config_path = os.getenv(
            "ETL_CONFIG_PATH",
            "/app/config/config.yaml"
        )
    try:
        with open(config_path, 'r') as f:
            cfg = yaml.safe_load(f)
    except FileNotFoundError:
        logger.error(f"Config file not found: {config_path}")
        sys.exit(1)
    except yaml.YAMLError as e:
        logger.error(f"Failed to parse config file: {e}")
        sys.exit(1)
    logging.config.dictConfig(cfg.get("etl").get("logging", {}))
    logger = logging.getLogger(__name__)
    logger.info("Starting Cleaning service")

    os.makedirs("sessions", exist_ok=True)
    app = create_app()
    #uvicorn.run(app, host=cfg["etl"]["host"], port=cfg["etl"]["port"])
    config = uvicorn.Config(
        app,
        host=cfg["etl"]["host"],
        port=cfg["etl"]["port"],
        log_config=cfg.get("etl").get("logging", {}),
    )
    server = uvicorn.Server(config)
    await server.serve()

if __name__ == "__main__":
    asyncio.run(main())