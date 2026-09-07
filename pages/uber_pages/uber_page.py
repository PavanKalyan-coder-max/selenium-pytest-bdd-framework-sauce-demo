from pages.base_page import BasePage
from locators.uber.uber_locators import UberSupplierLocator
from selenium.webdriver.common.by import By

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

    def click_filter(self):
        self.click(UberSupplierLocator.FILTER)

    def click_checkboxes(self, index):
       # checkboxes = self.click(UberSupplierLocator.FILTER_CHECKBOXES)
       # checkboxes[index].click()

       checkboxes = self.driver.find_elements(
           *UberSupplierLocator.FILTER_CHECKBOXES
       )

       checkboxes[index].click()

    def click_apply(self):
        self.click(UberSupplierLocator.CLICK_APPLY)

    def click_add_vehicle(self):
        self.click(UberSupplierLocator.ADD_VEHICLE)

    def add_vehicle_name(self, text):
        self.enter_text(UberSupplierLocator.ADD_VEHICLE_NAME, "fleetapp")

    def add_optional_name(self, text):
        self.enter_text(UberSupplierLocator.ADD_OPTIONAL_ID, "hey")

    def add_document_file(self, filename):
        self.upload_file(
            UberSupplierLocator.ADD_DOCUMENT,
            filename
        )

    def click_submit_button(self):
        self.click(UberSupplierLocator.CLICK_SUBMIT_BUTTON)


    def verify_vehicle_added(self):
        actual = self.get_text(UberSupplierLocator.VEHICLE_ADDED)

        expected = "PROD"

        assert actual == expected
        print("vehicle added")



    def click_tickets(self):
        self.click(UberSupplierLocator.TICKETS)


    def create_new_ticket(self):
        self.click(UberSupplierLocator.NEW_TICKET)

    def choose_vehicle(self):
        self.select_custom_dropdown(
            UberSupplierLocator.SELECT_VEHICLE,
            UberSupplierLocator.TEST1
        )

    def choose_issue_type(self):
        self.select_custom_dropdown(UberSupplierLocator.SELECT_ISSUE_TYPE, UberSupplierLocator.LOST_ITEM)

    def click_on_submmit_and_claim(self):
        self.click(UberSupplierLocator.SUBMIT_AND_CLAIM)

    def enter_description(self, text):
        self.enter_text(UberSupplierLocator.DESCRIPTION, "uber@123")


    def click_driver(self):
        self.click(UberSupplierLocator.DRIVER)

    def click_add_driver(self):
        self.click(UberSupplierLocator.ADD_DRIVER)

    def add_phone_number(self):
        self.enter_text(UberSupplierLocator.ADD_PHONE_NUMBER, "9700355208")

    def add_email_id(self):
        self.enter_text(UberSupplierLocator.ADD_EMAIL_ID, "ubertestdriver07@gmail.com")

    def add_first_name(self):
        self.enter_text(UberSupplierLocator.FIRST_NAME, "Autodriver1")

    def add_last_name(self):
        self.enter_text(UberSupplierLocator.LAST_NAME, "Autodriver2")

    def submit_add_driver(self):
        self.click(UberSupplierLocator.ADD_NEW_DRIVER)
