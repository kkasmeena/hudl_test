from behave import step
from locators.LoginPage import LoginPageLocators
from locators.HudlPage import HudlPageLocators
from data.UserData import UserData
from CommonSteps import driver

@step('User navigates to login page')
def step_impl(context):
    element = driver.find_element(*HudlPageLocators.LOGIN_BUTTON).click()
    element = driver.find_element(*HudlPageLocators.HUDL_LOGIN).click()

@step('Email address should be auto filled in')
def step_impl(context):
    expected_email_address = UserData.EMAIL_ADDRESS
    element = driver.find_element(*LoginPageLocators.EMAIL_ADDRESS_FIELD)
    assert element.text == expected_email_address