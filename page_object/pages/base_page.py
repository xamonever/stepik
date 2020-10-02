from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from stepik.page_object import BasePageLocators


class BasePage:

    def __init__(self, wd, url, timeout=10):
        self.wd = wd
        self.url = url
        self.wd.implicitly_wait(timeout)

    def open(self):
        self.wd.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.wd, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.wd, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_login_page(self):
        link = self.wd.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def go_to_basket_page(self):
        link = self.wd.find_element(*BasePageLocators.BASKET_LINK)
        link.click()







