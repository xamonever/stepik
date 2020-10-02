import math

from selenium.common.exceptions import NoAlertPresentException

from stepik.page_object import BasePage
from stepik.page_object import ProductPageLocators


class ProductPage(BasePage):

    def solve_quiz_and_get_code(self):
        alert = self.wd.switch_to.alert
        x = alert.text.split()[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.wd.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def check_promt_in_url(self):
        assert "promo" in self.wd.current_url, "'promo' not in url"

    def add_product_to_cart(self):
        el = self.wd.find_element(*ProductPageLocators.PRODUCT_PAGE__ADD_TO_CART)
        el.click()

    def check_added_to_cart_item_name(self):
        item_name = self.wd.find_element(*ProductPageLocators.PRODUCT_PAGE__ITEM_NAME).text
        added_title = self.wd.find_element(*ProductPageLocators.PRODUCT_PAGE__CART_ADDED_TITLE).text
        assert item_name == added_title, f'expected {item_name} in message, got {added_title}'

    def check_cart_total_cost_after_adding(self):
        item_price = self.wd.find_element(*ProductPageLocators.PRODUCT_PAGE__ITEM_PRICE).text
        cart_total_cost = self.wd.find_element(*ProductPageLocators.PRODUCT_PAGE__CART_TOTAL_COST).text
        assert item_price == cart_total_cost, f'expected {item_price} in message, got {cart_total_cost}'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is disappeared, but should not be"












