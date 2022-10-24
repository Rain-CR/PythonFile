
from behave import *


@given("I am on the home page")
def step_impl(context):
    context.browser.driver.get("https://the-internet.herokuapp.com/")


@when("I click the link for Add/Remove Elements")
def step_impl(context):
    add_remove_elements = context.browser.get_add_remove_link()
    add_remove_elements.click()


@then("I am redirected to the 'add_remove_elements' page")
def step_impl(context):
    redirect_link = context.browser.get_current_url()
    expected_url = "https://the-internet.herokuapp.com/add_remove_elements/"
    assert redirect_link == expected_url


@when("I click the link for checkbox")
def step_impl(context):
    checkbox_link = context.browser.get_checkboxes_link()
    checkbox_link.click()


@then("I am redirected to the 'checkbox' page")
def step_impl(context):
    redirect_link = context.browser.get_current_url()
    expected_url = "https://the-internet.herokuapp.com/checkboxes"
    assert redirect_link == expected_url


@when("I click the link for Form authentication")
def step_impl(context):
    form_link = context.browser.get_form_authentication_link()
    form_link.click()


@then("I am redirected to the 'Form authentication' page")
def step_impl(context):
    redirect_link = context.browser.get_current_url()
    expected_url = "https://the-internet.herokuapp.com/login"
    assert redirect_link == expected_url
