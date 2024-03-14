from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self,driver):
        self.driver = driver

    country = (By.CSS_SELECTOR, "#country")
    countries = (By.XPATH, "//div[@class='suggestions']/ul/li")
    primary_checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchase_button = (By.CSS_SELECTOR, ".btn-success")

    def enter_country(self, name):
        return self.driver.find_element(*ConfirmPage.country).send_keys(name)

    def get_countries_list(self):
        return self.driver.find_elements(*ConfirmPage.countries)

    def get_checkbox_primary(self):
        return self.driver.find_element(*ConfirmPage.primary_checkbox)

    def confirm_purchase(self):
        return self.driver.find_element(*ConfirmPage.purchase_button)
