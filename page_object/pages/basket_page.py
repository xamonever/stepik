from stepik.page_object import BasePage
from stepik.page_object import BasketPageLocators


class BasketPage(BasePage):

    def should_be_massage_empty(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_FOR_EMPTY_BASKET)

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS)









