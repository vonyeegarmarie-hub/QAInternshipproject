from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@when('Click on the settings option')
def click_settings(context):
    context.app.settings_page.click_settings()
    sleep(5)

@then('Verify the right page opens')
def verify_settings_page(context):
    context.app.settings_page.verify_settings_page('test+marie+careerist')

@then('Verify there are 18 options for the settings')
def verify_options_count(context):
    context.app.settings_page.verify_settings_options_count(18)

@then('Verify the “connect the company” button is available')
def verify_company(context):
    context.app.settings_page.verify_company()