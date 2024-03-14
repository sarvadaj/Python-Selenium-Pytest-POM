import time

import pytest
from selenium.webdriver.support.select import Select

from TestData.TestDataHome import TestDataHome
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
from selenium.webdriver.common.by import By


class TestHome(BaseClass):

    def test_home_form(self, getData):
        homepage = HomePage(self.driver)
        homepage.get_name().send_keys(getData["firstname"])
        homepage.get_email().send_keys(getData["lastname"])
        time.sleep(5)
        homepage.get_password().send_keys("123456789")
        homepage.get_checkbox().click()
        time.sleep(5)
        self.select_option_by_text(homepage.get_gender_select(), getData["gender"])
        # dropdown = Select(self.driver.find_element(By.ID,"exampleFormControlSelect1"))
        # dropdown.select_by_visible_text("Male")
        # dropdown.select_by_index(1)
        time.sleep(5)
        homepage.get_birthdate().send_keys("1992-01-08")
        homepage.click_submit_button().click()
        self.driver.refresh()

    @pytest.fixture(params=TestDataHome.get_test_data("TestCase1"))
    def getData(self, request):
        return request.param
