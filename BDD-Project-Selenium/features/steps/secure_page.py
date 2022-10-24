from behave import *
import time


@given("I connect with correct user and password")
def step_impl(context):
    context.browser.driver.get("https://the-internet.herokuapp.com/login")
    time.sleep(1)
    user_name = context.browser.get_username_element()
    user_name.send_keys("tomsmith")
    password = context.browser.get_password_element()
    password.send_keys("SuperSecretPassword!")
    login_button = context.browser.get_login_button()
    login_button.click()


@when("Check if the  message: ' You logged into a secure area!' is displayed")
def step_impl(context):
    secure_area_message = context.browser.get_alert_secure_area().text
    expected_message = "You logged into a secure area!"
    assert expected_message in secure_area_message


@then("I click the logout button")
def step_impl(context):
    logout_button = context.browser.get_logout_bt()
    logout_button.click()
