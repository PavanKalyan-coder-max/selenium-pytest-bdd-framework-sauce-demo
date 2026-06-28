from pages.base_page import BasePage
from locators.checkout_locators import CheckoutLocators


class CheckoutPage(BasePage):

    def enter_first_name(self, first_name):
        self.enter_text(
            CheckoutLocators.FIRST_NAME,
            first_name
        )

    def enter_last_name(self, last_name):
        self.enter_text(
            CheckoutLocators.LAST_NAME,
            last_name
        )

    def enter_postal_code(self, postal_code):
        self.enter_text(
            CheckoutLocators.POSTAL_CODE,
            postal_code
        )

    def click_continue(self):
        self.click(
            CheckoutLocators.CONTINUE_BUTTON
        )

    def click_finish(self):
        self.click(
            CheckoutLocators.FINISH_BUTTON
        )

    def fill_checkout_information(
            self,
            first_name,
            last_name,
            postal_code
    ):

        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal_code)

        self.click_continue()