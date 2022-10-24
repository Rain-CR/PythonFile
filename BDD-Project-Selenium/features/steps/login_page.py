from behave import *


@given("I am on the login page")
def step_impl(context):
    context.browser.driver.get("https://the-internet.herokuapp.com/login")


@when("I enter a correct username")
def step_impl(context):
    user_name = context.browser.get_username_element()
    user_name.send_keys("tomsmith")


@when("I enter a correct password")
def step_impl(context):
    password = context.browser.get_password_element()
    password.send_keys("SuperSecretPassword!")


@then("I click on the login button")
def step_impl(context):
    login_button = context.browser.get_login_button()
    login_button.click()
