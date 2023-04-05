from selenium.webdriver.common.by import By

class HomePageLocators(object):
    HOME_BUTTON = (By.CSS_SELECTOR, "[data-qa-id='webnav-globalnav-home']")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "[data-qa-id='webnav-usermenu-logout']")
    USERNAME_BUTTON = (By.CLASS_NAME, 'hui-globaluseritem__display-name')


