import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def checkPresence(self, path):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(path))

    def select_option_by_text(self, locator, text):
        dropdown = Select(locator)
        dropdown.select_by_visible_text(text)


    def getLogger(self):
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)

        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s :%(name)s :%(message)s ")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.debug("Debug mode")
        logger.setLevel(logging.INFO)
        return logger


