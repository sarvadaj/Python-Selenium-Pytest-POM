from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(executable_path="C://Users//GS-0853//Downloads//chromedriver-win64 (1)//chromedriver-win64//chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://rahulshettyacademy.com/angularpractice/")


