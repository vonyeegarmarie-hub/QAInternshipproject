from pages.log_in_page import LoginPage
from pages.main_page import MainPage
from pages.settings_page import SettingsPage



class Application:

    def __init__(self, driver):

        self.main_page = MainPage(driver)
        self.log_in_page = LoginPage(driver)
        self.settings_page = SettingsPage(driver)