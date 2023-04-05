from selenium.webdriver.common.by import By

class HudlPageLocators(object):
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[data-qa-id='login-select']")
    HUDL_LOGIN = (By.CSS_SELECTOR, "[data-qa-id='login-hudl']")

