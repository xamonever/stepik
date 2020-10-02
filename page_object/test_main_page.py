from stepik.page_object.pages.basket_page import BasketPage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com"


# @pytest.mark.now
def test_guest_cant_see_product_in_basket_opened_from_main_page(wd):
    page = MainPage(wd, link)
    page.open()
    page.go_to_basket_page()

    basket_page = BasketPage(wd, wd.current_url)
    basket_page.should_be_empty_basket()
    basket_page.should_be_massage_empty()


def test_guest_can_go_to_login_page(wd):
    page = MainPage(wd, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(wd, wd.current_url)
    login_page.should_be_login_page()


def test_guest_should_see_login_link(wd):
    page = MainPage(wd, link)
    page.open()
    page.should_be_login_link()
