from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    VIEW_BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini .btn-group > a")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTRATION_FORM = (By.ID, "register_form")
    EMAIL_FIELD = (By.ID, "id_registration-email")
    PASSWORD_FIELD = (By.ID, "id_registration-password1")
    CONFIRM_PASSWORD_FIELD = (By.ID, "id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_page .product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_page .product_main > .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div.alert:nth-child(1)")
    PRODUCT_NAME_MESSAGE = (By.CSS_SELECTOR, "#messages div.alert:nth-child(1) strong")
    PRODUCT_PRICE_MESSAGE = (By.CSS_SELECTOR, "#messages div.alert:nth-child(3) strong")


class BasketPageLocators:
    EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner > p")


