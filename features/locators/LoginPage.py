from selenium.webdriver.common.by import By

class LoginPageLocators(object):
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[data-qa-id='login-btn']")
    EMAIL_ADDRESS_FIELD = (By.CSS_SELECTOR, "[data-qa-id='email-input']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "[data-qa-id='password-input']")
    LOGIN_ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-qa-id='error-display']")
    REMEMBER_ME_CHECKBOX_LABEL = (By.CSS_SELECTOR, "[data-qa-id='remember-me-checkbox-label']")
    REMEMBER_ME_CHECKBOX = (By.CSS_SELECTOR, "[data-qa-id='remember-me-checkbox']")
    LOGIN_WITH_ORGANISATION_BUTTON = (By.CSS_SELECTOR, "[data-qa-id='log-in-with-organization-btn']")

class LoginPageCopy(object):
    LOGIN_ERROR_TEXT = ("We didn't recognize that email and/or password.")
    LOGIN_WITH_ORGANISATION_ERROR_TEXT = ("This account can't log in with an organization yet. Please log in using your email and password.")
