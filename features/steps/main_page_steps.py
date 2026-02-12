from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open the main page https://soft.reelly.io')
def open_main(context):
    context.app.main_page.open_main_page()
    sleep(10)