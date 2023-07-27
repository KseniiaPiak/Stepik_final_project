from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTRATION_FORM = (By.ID, "register_form")


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_page .product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_page .product_main > .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div.alert:nth-child(1)")
    PRODUCT_NAME_MESSAGE = (By.CSS_SELECTOR, "#messages div.alert:nth-child(1) strong")
    PRODUCT_PRICE_MESSAGE = (By.CSS_SELECTOR, "#messages div.alert:nth-child(3) strong")

