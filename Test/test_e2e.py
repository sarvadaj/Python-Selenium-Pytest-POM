import time
from selenium.webdriver.common.by import By
from pageObjects.CheckOutPage import CheckOutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass

class TestOne(BaseClass):
    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        homePage.getHome()
        checkoutPage = CheckOutPage(self.driver)
        confirmPage = ConfirmPage(self.driver)
        products = checkoutPage.getCardTitles()

        for product in products:

            productName = product.find_element(By.XPATH, "div/h4/a").text
            log.info(productName)

            if productName == "Blackberry":
                product.find_element(By.XPATH, "div/button").click()
                time.sleep(2)

        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

        checkoutPage.click_checkout_button().click()
        time.sleep(3)
        total = checkoutPage.get_total_amount().text
        print(total)

        checkoutPage.click_confirm_checkOut().click()
        confirmPage.enter_country("Ind")

        self.checkPresence(CheckOutPage.india_in_list)

        #wait = WebDriverWait(self.driver, 6)
        #wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='suggestions']/ul/li/a")))

        countries = confirmPage.get_countries_list()


        print(len(countries))
        for country in countries:
            if country.find_element(By.XPATH, "a").text == "India":
                time.sleep(1)
                country.find_element(By.XPATH, "a").click()
                break
        confirmPage.get_checkbox_primary().click()
        confirmPage.confirm_purchase().click()
        message = self.driver.find_element(By.CSS_SELECTOR, ".alert-success").text
        assert "Success" in message



'''
        products = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']/div/h4/a")
        # products = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
        # products = self.find_elements(By.XPATH, "//div[@class='card h-100']")
        print(len(products))
        for p in products:
            name = p.text
            print(name)
'''
