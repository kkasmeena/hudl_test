from behave import step
from locators.LoginPage import LoginPageLocators, LoginPageCopy
from locators.HomePage import HomePageLocators
from data.UserData import UserData
from CommonSteps import (driver, OpenBrowserToURL, wait)
from data.Urls import Urls
from selenium.webdriver.support import expected_conditions as EC


@step('User is on login page')
def step_impl(context):
    OpenBrowserToURL(Urls.HUDL_LOGIN_PAGE)
    assert driver.find_element(*LoginPageLocators.LOGIN_BUTTON)

@step('User enters valid email address')
def step_impl(context):
    element = driver.find_element(*LoginPageLocators.EMAIL_ADDRESS_FIELD)
    element.clear()
    element.send_keys(*UserData.EMAIL_ADDRESS)

@step('User enters invalid email address')
def step_impl(context):
    element = driver.find_element(*LoginPageLocators.EMAIL_ADDRESS_FIELD)
    element.clear()
    element.send_keys(*UserData.INVALID_EMAIL_ADDRESS)

@step('User enters unregistered email address')
def step_impl(context):
    element = driver.find_element(*LoginPageLocators.EMAIL_ADDRESS_FIELD)
    element.clear()
    element.send_keys(*UserData.UNREGISTERED_EMAIL_ADDRESS)

@step('User enters valid password')
def step_impl(context):
    element = driver.find_element(*LoginPageLocators.PASSWORD_FIELD)
    element.clear()
    element.send_keys(*UserData.PASSWORD)

@step('Clicks Login')
def step_impl(context):
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

@step('User is logged in successfully')
def step_impl(context):
    assert wait.until(EC.element_to_be_clickable(HomePageLocators.HOME_BUTTON))

@step('Login error message is displayed')
def step_impl(context):
    assert wait.until(EC.text_to_be_present_in_element(LoginPageLocators.LOGIN_ERROR_MESSAGE, LoginPageCopy.LOGIN_ERROR_TEXT))
    assert driver.find_element(*LoginPageLocators.LOGIN_BUTTON).is_enabled() == False

@step('Selects remember me')
def step_impl(context):
    driver.find_element(*LoginPageLocators.REMEMBER_ME_CHECKBOX_LABEL).click()
    checkbox = driver.find_element(*LoginPageLocators.REMEMBER_ME_CHECKBOX)
    assert checkbox.is_selected()
    
@step('User fills in valid credentials')
def step_impl(context):
    context.execute_steps('''
        when User enters valid email address
        and User enters valid password
    ''')