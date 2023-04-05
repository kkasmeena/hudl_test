from selenium import webdriver


def SetUp():
    driver = webdriver.Chrome()
    return driver

def OpenBrowserToURL(url):
    driver.get(url)

driver = SetUp()

