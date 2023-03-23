from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def fill_email_field(self):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        '''Тут можно вставить свой email'''
        email_field.send_keys("lllax87@yandex.ru")

    def click_sign_in_button(self):
        sign_in_button = self.browser.find_element(*LoginPageLocators.SIGN_IN_BUTTON)
        sign_in_button.click()

    def fill_password_field(self):
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        '''Тут можно вставить свой пароль'''
        password_field.send_keys("lax8886")