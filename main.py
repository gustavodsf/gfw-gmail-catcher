import logging
import os

from src.config import Config
from src.manager import Manager

if __name__ == "__main__":
    config = Config()
    configParams = config.read()
    logging.basicConfig(
        filename="{}gfw-catcher.log".format(os.getenv("WRITE_PATH")),
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        filemode="a",
        datefmt="%d/%m/%Y %I:%M:%S %p",
        level=logging.INFO,
    )

    manager = Manager(configParams)
    manager.run_capture()

    """
    schedule.every().day.at(configParams.get("exec_time")).do(manager.run_capture)

    while True:
        schedule.run_pending()
    """
