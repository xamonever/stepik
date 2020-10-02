import time
import pytest

from stepik.page_object import promo_links
from stepik.page_object.pages.basket_page import BasketPage
from stepik.page_object import ProductPage


@pytest.mark.parametrize('link', promo_links)
def test_guest_can_add_product_to_basket(wd, link):

    try:
        page = ProductPage(wd, link, 5)
        page.open()
        page.check_promt_in_url()
        page.add_product_to_cart()
        page.solve_quiz_and_get_code()
        page.check_added_to_cart_item_name()
        page.check_cart_total_cost_after_adding()
    finally:
        time.sleep(1)


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(wd):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(wd, link, 0)
    page.open()
    page.add_product_to_cart()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(wd):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(wd, link, 0)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(wd):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(wd, link, 0)
    page.open()
    page.add_product_to_cart()
    page.should_be_disappeared_success_message()


def test_guest_should_see_login_link_on_product_page(wd):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(wd, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(wd):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(wd, link)
    page.open()
    page.go_to_login_page()


# @pytest.mark.now
def test_guest_cant_see_product_in_basket_opened_from_product_page(wd):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(wd, link)
    page.open()
    page.go_to_basket_page()

    basket_page = BasketPage(wd, wd.current_url)
    basket_page.should_be_empty_basket()
    basket_page.should_be_massage_empty()







