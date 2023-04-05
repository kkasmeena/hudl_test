from selenium.webdriver.common.by import By

class LoginPageLocators(object):
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[data-qa-id='login-btn']")
    EMAIL_ADDRESS_FIELD = (By.CSS_SELECTOR, "[data-qa-id='email-input']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "[data-qa-id='password-input']")
    LOGIN_ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-qa-id='error-display']")
    REMEMBER_ME_CHECKBOX_LABEL = (By.CSS_SELECTOR, "[data-qa-id='remember-me-checkbox-label']")
    REMEMBER_ME_CHECKBOX = (By.CSS_SELECTOR, "[data-qa-id='remember-me-checkbox']")

class LoginPageCopy(object):
    LOGIN_ERROR_TEXT = ("We didn't recognize that email and/or password.")
