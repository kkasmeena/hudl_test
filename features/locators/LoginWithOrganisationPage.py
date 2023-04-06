from selenium.webdriver.common.by import By

class LoginWithOrganisationLocators(object):
    EMAIL_FIELD = (By.ID, "uniId_1")
    LOG_IN_BUTTON = (By.CSS_SELECTOR, "[data-qa-id='log-in-with-sso']")
    