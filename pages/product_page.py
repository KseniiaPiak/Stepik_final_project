from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        basket_button.click()

    def should_be_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "Basket button not found"

    def should_be_alert_product_name_message(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME_MESSAGE), "Product name message not found"

    def should_be_alert_product_price_message(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE_MESSAGE), "Product price message not found"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared"

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def check_equals_product_name(self):
        product_name = self.get_product_name()
        product_name_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_MESSAGE)
        assert product_name == product_name_message.text, "Product name is not equal"

    def check_equals_product_price(self):
        product_price = self.get_product_price()
        product_price_message = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_MESSAGE)
        assert product_price == product_price_message.text, "Product price is not equal"


