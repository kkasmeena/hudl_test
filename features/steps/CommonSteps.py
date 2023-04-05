from selenium import webdriver
from data.Urls import Urls


def SetUp():
    driver = webdriver.Chrome()
    return driver
## does this now open  two browsers?
def OpenBrowserToURL(url):
   driver.get(url)

driver = SetUp()

