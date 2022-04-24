import logging

import requests
from retry import retry


class Download(object):
    def __init__(self):
        self.logger = logging.getLogger("DOWNLOAD")

    @retry(exceptions=Exception, delay=20, tries=100)
    def getData(self, url):
        print("Start to download the csv file")
        self.logger.info("Start to download the csv file")
        response = requests.get(url)
        if response.status_code >= 200 and response.status_code <= 299:
            print("Donwload.content {}".format(response.content[0:40]))
            self.logger.debug(
                "Donwload.content {}".format(response.content[0:20])
            )
            return response.content
        print("Problem to download the csv file, the system will retry in 20s.")
        self.logger.debug(
            "Problem to download the csv file, the system will retry in 20s."
        )
        raise Exception("Problem to get data from url.")
