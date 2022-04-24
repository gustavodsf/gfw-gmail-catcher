import logging
from datetime import date


class CsvFile(object):
    def __init__(self):
        self.logger = logging.getLogger("CSV-FILE")

    def save(self, content, file_name="file", path="./"):
        print("Starting saving the content into a CSV File")
        self.logger.info("Starting saving the content into a CSV File")
        current_date = date.today()
        with open(
            "{}{}-{}.csv".format(path, file_name, current_date), "wb"
        ) as file:
            file.write(content)
        file.close()
        print("Finished saving the content into a CSV File")
        self.logger.info("Finished saving the content into a CSV File")
