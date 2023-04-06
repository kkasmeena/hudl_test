from behave import step
from data.UserData import UserData
from CommonSteps import (driver)
from locators.LoginWithOrganisationPage import LoginWithOrganisationLocators

@step('User enters their email address')
def step_impl(context):
    element = driver.find_element(*LoginWithOrganisationLocators.EMAIL_FIELD)
    element.clear()
    element.send_keys(*UserData.EMAIL_ADDRESS)

@step('Clicks login on organisation page')
def step_impl(context):
    driver.find_element(*LoginWithOrganisationLocators.LOG_IN_BUTTON).click()

