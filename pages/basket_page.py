from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET), "Basket is not empty"

    def should_be_empty_basket_message(self, message):
        empty_basket_message = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET)
        print(empty_basket_message.text)
        assert empty_basket_message.text == message, \
            "Empty basket message is not equal web-site language"

