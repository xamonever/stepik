from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini span a")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")

    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, "#content_inner div.basket-items>div.row")
    MESSAGE_FOR_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner>p>a")


class LoginPageLocators:
    EMAIL_FIELD = (By.CSS_SELECTOR, 'div.register_form input[name="registration-email"]')
    PASSWORD_FIELD = (By.CSS_SELECTOR, 'div.register_form input[name="registration-password1"]')
    CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, 'div.register_form input[name="registration-password2"]')

    SUBMIT_BUTTON = (By.CSS_SELECTOR, '*[value="Register"]')


class MainPageLocators:
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    PRODUCT_PAGE__ITEM_NAME = (By.XPATH, '//h1')
    PRODUCT_PAGE__ITEM_PRICE = (By.XPATH, '//div[./h1]/p[@class="price_color"]')
    PRODUCT_PAGE__ADD_TO_CART = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_PAGE__CART_ADDED_TITLE = (By.XPATH,
                                '//div[@id="messages"]/div/div[contains(., "було додано до Вашого кошику")]/strong')
    PRODUCT_PAGE__CART_TOTAL_COST = (By.CSS_SELECTOR, 'div#messages div.alert-info p strong')

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div#messages div')











