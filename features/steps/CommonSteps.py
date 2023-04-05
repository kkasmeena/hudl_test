from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


def SetUp():
    driver = webdriver.Chrome()
    return driver

def OpenBrowserToURL(url):
    driver.get(url)

driver = SetUp()

wait = WebDriverWait(driver, 10)
