from allure_behave.utils import scenario_name
from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
#from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from app.application import Application


def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """
    #driver_path = ChromeDriverManager().install()
    #service = Service(driver_path)
    #options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # options.add_argument('--disable-notifications')

    # driver_path = GeckoDriverManager().install()
    # service = Service(driver_path)

     #options = webdriver.FirefoxOptions()
    #context.driver = webdriver.Firefox(service=service)
    #context.driver = webdriver.Chrome(service=service, options=options)

    ## BROWSERSTACK ###
    # # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    bs_user = 'marievonyeegar_TcWNpG'  # Add here your user key
    bs_key = '8VY9sK4LouQDE7qQhoH7'  # Add here your pass key
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    options = Options()
    bstack_options = {
        'os': 'OS X',  ## OS X for macOS if Windows just add Windows
        'osVersion': 'Big Sur',  # Specify the version you want to use
        'browserName': 'Firefox',
        'sessionName': scenario_name,
        'video': 'true',
        'seleniumLogs': 'true',
        'networkLogs': 'true'
    }
    options.set_capability('bstack:options', bstack_options)
    context.driver = webdriver.Remote(command_executor=url, options=options)
    context.driver.maximize_window()
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