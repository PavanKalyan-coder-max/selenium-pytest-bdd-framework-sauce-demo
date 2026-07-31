from pages.base_page import BasePage
from locators.uber.uber_locators import UberSupplierLocator


class uberpage(BasePage):

    def uber_page(self, email):
        self.enter_text(UberSupplierLocator.EMAIL, email)

    def  uber_page_submit(self):
        self.click(UberSupplierLocator.SUBMIT)

    def click_more_options(self):
        self.click(UberSupplierLocator.MORE_OPTIONS)


    def click_password_option(self):
        self.click(UberSupplierLocator.CLICK_PASSWORD_OPTION)


    def enter_password(self, text):
        self.enter_text(UberSupplierLocator.PASSWORD, text)

    def click_next(self):
        self.click(UberSupplierLocator.NEXT)

    def click_vehicles_beta(self):
        self.click(UberSupplierLocator.VEHICLES_BETA)

