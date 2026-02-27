from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import Page

class SettingsPage(Page):
    Settings_BTN= (By.CSS_SELECTOR, "a[href='https://soft.reelly.io/settings']")
    PROFILE_SETTING = (By.CSS_SELECTOR, ".settings-profile-block")                 #(By.CSS_SELECTOR, ".name-prifile-setting")
    SETTINGS_OPTIONS = (By.CSS_SELECTOR, ".page-setting-block.w-inline-block")
    COMPANY_BTN = (By.XPATH, "//div[@class='get-free-period menu' and text()='Connect the company']")
    MENU_BTN= (By.CSS_SELECTOR, "a.new-market-menu-button._1.w-inline-block")
    MARKET_OFFERS_BTN = (By.XPATH, "//a[@href='https://soft.reelly.io/']")


    def click_menu(self):
        menu_element = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(self.MENU_BTN)
        )
        menu_element.click()


    def click_market_offers(self):
        market_offers_element = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.MARKET_OFFERS_BTN)
        )
        market_offers_element.click()


    def click_settings(self):
        sleep(3)
        settings_element = self.find_element(*self.Settings_BTN)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", settings_element)
        sleep(1)
        self.click(*self.Settings_BTN)

    def verify_settings_page(self, username):
        #profile_element = (
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(self.PROFILE_SETTING)
        )
        #     lambda driver: username in driver.page_source
        # )
            # EC.text_to_be_present_in_element(self.PROFILE_SETTING, username)
        # )
        # actual_text = (profile_element.text or
        #            profile_element.get_attribute("textContent") or
        #            profile_element.get_attribute("innerText"))
        #     assert profile_element, f"Expected {username} not found on settings page"


    def verify_settings_options_count(self, expected_count):
        options = self.find_elements(*self.SETTINGS_OPTIONS)
        actual_count = len(options)
        assert actual_count == expected_count, \
            f"Expected {expected_count} options, but got {actual_count}"

    def verify_company(self):
        company_element = self.find_element(*self.COMPANY_BTN)
        assert company_element.is_displayed(), "Connect the company button is not visible"