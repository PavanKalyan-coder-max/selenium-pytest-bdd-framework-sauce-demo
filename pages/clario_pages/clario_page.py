from selenium.webdriver import Keys
from pages.base_page import BasePage
from locators.clario.clario_locators import Clariolocators


class ClarioPage(BasePage):

    # def create_account(self):
    #     self.click(Clariolocators.CREATE_ACCOUNT, "clicked on create account")
    #
    # def enter_email(self, email):
    #     self.enter_text(Clariolocators.EMAIL, email)

    def create_account(self):
        self.click(
            Clariolocators.CREATE_ACCOUNT,
            "Clicked on Create Account"
        )

    def enter_email(self, email):
        self.enter_text(
            Clariolocators.EMAIL,
            email
        )

    def enter_confirm_email(self, confirm_email):
        self.enter_text(
            Clariolocators.CONFIRM_EMAIL,
            confirm_email
        )

    def enter_first_name(self, first_name):
        self.enter_text(
            Clariolocators.FIRST_NAME,
            first_name
        )

    def enter_last_name(self, last_name):
        self.enter_text(
            Clariolocators.LAST_NAME,
            last_name
        )

    def enter_password(self, password):
        self.enter_text(
            Clariolocators.PASSWORD,
            password
        )

    def enter_confirm_password(self, confirm_password):
        self.enter_text(
            Clariolocators.CONFIRM_PASSWORD,
            confirm_password
        )
