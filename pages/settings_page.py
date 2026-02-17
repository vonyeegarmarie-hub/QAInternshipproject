from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class SettingsPage(Page):
    Settings_BTN= (By.CSS_SELECTOR, "a[href='https://soft.reelly.io/settings']")
    PROFILE_SETTING = (By.CSS_SELECTOR, ".name-prifile-setting")
    SETTINGS_OPTIONS = (By.CSS_SELECTOR, ".page-setting-block.w-inline-block")
    COMPANY_BTN = (By.XPATH, "//div[@class='get-free-period menu' and text()='Connect the company']")



    def click_settings(self):
        sleep(3)
        settings_element = self.find_element(*self.Settings_BTN)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", settings_element)
        sleep(1)
        self.click(*self.Settings_BTN)

    def verify_settings_page(self, expected_text):
        actual_text = self.find_element(*self.PROFILE_SETTING).text
        assert expected_text == actual_text, \
            f"Expected {expected_text}, but got actual {actual_text}"

    def verify_settings_options_count(self, expected_count):
        options = self.find_elements(*self.SETTINGS_OPTIONS)
        actual_count = len(options)
        assert actual_count == expected_count, \
            f"Expected {expected_count} options, but got {actual_count}"

    def verify_company(self):
        company_element = self.find_element(*self.COMPANY_BTN)
        assert company_element.is_displayed(), "Connect the company button is not visible"