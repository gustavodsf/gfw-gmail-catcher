import logging
from os import getenv

from src.csv_file import CsvFile
from src.download import Download
from src.gmail import Gmail


class Manager(object):
    def __init__(self, config):
        self.config = config
        self.mount()

    def mount(self):
        self.download = Download()
        self.csvFile = CsvFile()

        self.logger = logging.getLogger("MANAGER")
        print("Read Config Params")
        self.logger.info("Read Config Params")

        print("Create Gmail reader")
        self.logger.info("Create Gmail reader")
        self.gmail = Gmail(self.config)

        print("Add schedule task to capture the data")
        self.logger.info("Add schedule task to capture the data")

    def run_capture(self):
        print("start capture the forest data")
        self.logger.info("start capture the forest data")
        urlList = self.gmail.get_url_from_email()
        print("Found {} csv files to download".format(len(urlList)))
        self.logger.info("Found {} csv files to download".format(len(urlList)))
        count = 1
        # try:
        for url in urlList:
            content = self.download.getData(url)
            file_name = "{}-{}".format(count, self.config.get("file_name"))
            self.csvFile.save(
                content, path=getenv("WRITE_PATH"), file_name=file_name
            )
            print("fineshed capture the forest data")
            self.logger.info("fineshed capture the forest data")
            count += 1
        # except:
        #    print("Was not possible to download file from: {}".format(url))
        #    self.logger.error("Was not possible to download file from: {}".format(url))
