from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class LoginPage(Page):
    USERNAME_FIELD= (By.ID, 'email-2')
    PASSWORD_FIELD= (By.ID, 'field')
    CONT_BTN = (By.CLASS_NAME, "login-button")


    def enter_username(self):
        self.input_text('marievonyeegar@gmail.com', *self. USERNAME_FIELD)

    def enter_password(self):
        self.input_text('pythontest', *self. PASSWORD_FIELD)

    def click_cont_button(self):
        self.click(*self.CONT_BTN)
        sleep(6)
