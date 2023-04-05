from behave import step
from locators.HomePage import HomePageLocators
from locators.HudlPage import HudlPageLocators
from CommonSteps import (driver, wait)
from selenium.webdriver.support import expected_conditions as EC

@step('User logs out of account')
def step_impl(context):
    driver.find_element(*HomePageLocators.USERNAME_BUTTON).click()
    driver.find_element(*HomePageLocators.LOGOUT_BUTTON).click()
    assert wait.until(EC.visibility_of_element_located(HudlPageLocators.LOGIN_BUTTON))
