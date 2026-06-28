from pages.base_page import BasePage
from locators.cart_locators import CartLocators


class CartPage(BasePage):

    def click_checkout(self):

        self.click(
            CartLocators.CHECKOUT_BUTTON
        )