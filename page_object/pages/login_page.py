from .base_page import BasePage
from .locators import *


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.wd.current_url, '"login" not in url'

    def should_be_login_form(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_FORM), 'no login form'

    def should_be_register_form(self):
        assert self.is_element_present(*MainPageLocators.REGISTRATION_FORM), 'no register form'

    def register_new_user(self, email, password):
        self.wd.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(email)
        self.wd.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(password)
        self.wd.find_element(*LoginPageLocators.CONFIRM_PASSWORD_FIELD).send_keys(password)

        button_el = self.wd.find_element(*LoginPageLocators.SUBMIT_BUTTON)
        button_el.click()









