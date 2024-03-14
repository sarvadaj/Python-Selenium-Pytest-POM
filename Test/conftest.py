import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximised")
        # chrome_options.add_argument("headless")
        # chrome_options.add_argument("--ignore-certificate-errors")
        service = Service()
        driver = webdriver.Chrome(service=service, options=chrome_options)


    elif browser_name == "firefox:":
        print("Firefox Browser")

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


