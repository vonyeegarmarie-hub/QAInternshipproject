from allure_behave.utils import scenario_name
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from app.application import Application
from selenium import webdriver


def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """
    # mobile_emulation = {"deviceName": "Nexus 5"}
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    # chrome_options.add_argument("--disable-notifications")
    #
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service, options=chrome_options)



    ## BROWSERSTACK ###
    # # # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    bs_user = 'marievonyeegar_TcWNpG'
    bs_key = '8VY9sK4LouQDE7qQhoH7'
    url = f'https://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    options = webdriver.SafariOptions()
    options.set_capability('bstack:options', {
        "deviceName": "iPhone 14 Plus",
        "osVersion": "16",
        "realMobile": "true",
        "sessionName": scenario_name,
        "video": "true",
        "seleniumLogs": "true",
        "networkLogs": "true",
        "debug": "true",
    })
    options.set_capability("browserName", "safari")
    context.driver = webdriver.Remote(command_executor=url, options=options)

    #context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, timeout=10)
    context.app = Application(context.driver)

def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)

def before_step(context, step):
    print('\nStarted step: ', step)

def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)
# def after_scenario(context, feature):
#     context.driver.quit()

def after_scenario(context, scenario):
    if hasattr(context, 'driver'):
        context.driver.quit()