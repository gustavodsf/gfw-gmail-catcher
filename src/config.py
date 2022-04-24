import json
import logging


class Config(object):
    def __init__(self):
        self.logger = logging.getLogger("CONFIG")

    def read(self):
        with open("config.json") as file:
            data = json.load(file)
        file.close()
        print("Running code with following config {}".format(str(data)))
        self.logger.info(
            "Running code with following config {}".format(str(data))
        )
        return data
