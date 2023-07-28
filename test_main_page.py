import pytest

from pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.main_page import MainPage


@pytest.mark.skip
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.go_to_login_page()
    login_page = LoginPage(browser, link)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/"
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.should_be_view_basket_button()
    main_page.go_to_basket()
    basket_page = BasketPage(browser, link)
    basket_page.should_be_empty_basket()
    basket_page.should_be_empty_basket_message("Ваша корзина пуста Продолжить покупки")


