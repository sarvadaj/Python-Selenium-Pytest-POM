from selenium.webdriver.common.by import By


class CheckOutPage:
    def __init__(self, driver):
        self.driver = driver

    products = (By.XPATH, "//div[@class='card h-100']")
    add_buttons = (By.XPATH, "//div[@class='card h-100']/div/button")
    checkout_button = (By.CSS_SELECTOR, "a[class='nav-link btn btn-primary']")
    confirm_checkout = (By.XPATH, "//button[@class='btn btn-success']")
    total = (By.XPATH, "//td[@class='text-right']/h3")
    india_in_list = (By.XPATH, "//div[@class='suggestions']/ul/li/a")


    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.products)

    def getFooterAddButtons(self):
        return self.driver.find_element(*CheckOutPage.add_buttons)

    def click_checkout_button(self):
        return self.driver.find_element(*CheckOutPage.checkout_button)

    def click_confirm_checkOut(self):
        return self.driver.find_element(*CheckOutPage.confirm_checkout)

    def get_total_amount(self):
        return self.driver.find_element(*CheckOutPage.total)




