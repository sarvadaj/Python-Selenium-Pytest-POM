from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self,driver):
        self.driver = driver

    shop = (By.LINK_TEXT, "Shop")
    name = (By.NAME, "name")
    email = (By.NAME, "email")
    password = (By.CSS_SELECTOR,".form-control")
    checkbox = (By.ID, "exampleCheck1")
    gender = (By.ID,"exampleFormControlSelect1")
    birthdate = (By.NAME, "bday")
    submit_button = (By.XPATH, "//input[@class='btn btn-success']")


    def getHome(self):
        self.driver.find_element(*HomePage.shop).click()

    def get_name(self):
        return self.driver.find_element(*HomePage.name)

    def get_email(self):
        return self.driver.find_element(*HomePage.email)

    def get_password(self):
        return self.driver.find_element(*HomePage.password)

    def get_checkbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def get_gender_select(self):
        return self.driver.find_element(*HomePage.gender)

    def get_birthdate(self):
        return self.driver.find_element(*HomePage.birthdate)

    def click_submit_button(self):
        return self.driver.find_element(*HomePage.submit_button)



