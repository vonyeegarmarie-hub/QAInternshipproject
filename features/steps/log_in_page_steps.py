from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Log in to the page')
def log_in_page(context):

    context.app.log_in_page.enter_username()
    context.app.log_in_page.enter_password()
    context.app.log_in_page.click_cont_button()
    sleep(7)
