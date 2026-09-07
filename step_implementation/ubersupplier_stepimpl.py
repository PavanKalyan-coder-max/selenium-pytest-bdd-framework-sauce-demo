from pages.uber_pages.uber_page import uberpage
from config.config_reader import ConfigReader
from utilities import client


class Ubersuppimpl():

    def launch_application(self, client):
        client.driver.get(
            ConfigReader.get_uber_supplier_url()
        )

    def uber_page_email(self, client):

        uber_page_email_enter = uberpage(client.driver)
        uber_page_email_enter.uber_page(
            ConfigReader.get_uber_email()
        )


    def uber_submit(self,client):
        uber = uberpage(client.driver)
        uber.uber_page_submit()

    def click_on_more_options(self, client):

        Uber_more_options = uberpage(client.driver)
        Uber_more_options.click_more_options()


    def click_on_password_option(self, client):
        option = uberpage(client.driver)
        option.click_password_option()


    def click_on_password(self, client):
        click_password = uberpage(client.driver)
        click_password.enter_password(
            ConfigReader.get_uber_password()
        )

    def click_next_button(self, client):

        click = uberpage(client.driver)
        click.click_next()

    def click_vehicles_beta(self,client):
        vehicles_beta = uberpage(client.driver)
        vehicles_beta.click_vehicles_beta()


    def click_on_filter(self,client):
        page = uberpage(client.driver)
        page.click_filter()

    def test_all_filters(self, client):
        page = uberpage(client.driver)

        for index in range(31):

            page.click_filter()
            page.click_checkboxes(index)
            page.click_apply()

    def click_on_add_vehicle(self, client):
        page = uberpage(client.driver)
        page.click_add_vehicle()

    def add_vehicle_id(self, client):
        page = uberpage(client.driver)
        page.add_vehicle_name("Prod")

    def add_optional_id(self, client):
        page = uberpage(client.driver)
        page.add_optional_name("hey")

    def add_document_file_vehicle_registration(self, client):
        page = uberpage(client.driver)
        page.add_document_file(r"C:\Users\DELL\Downloads\uberss.PNG")

    def click_on_submit_button(self, client):
        page = uberpage(client.driver)
        page.click_submit_button()


    def verify_vehicle_added(self,client):
        page = uberpage(client.driver)
        page.verify_vehicle_added()

    def click_on_tickets(self,client):
        page = uberpage(client.driver)
        page.click_tickets()

    def create_new_ticket(self, client):
        page = uberpage(client.driver)
        page.create_new_ticket()


    def choose_vehicle(self, client):
        page = uberpage(client.driver)
        page.choose_vehicle()

    def choose_issue_type(self, client):
        page = uberpage(client.driver)
        page.choose_issue_type()

    def click_submt_and_claim(self, client):
        page = uberpage(client.driver)
        page.click_on_submmit_and_claim()

    def enter_description(self, client):
        page = uberpage(client.driver)
        page.enter_description("uber@123")

    def click_drivers(self,client):
        page = uberpage(client.driver)
        page.click_driver()

    def click_add_drivers(self,client):
        page = uberpage(client.driver)
        page.click_add_driver()

    def add_phone_number(self, client):
        page = uberpage(client.driver)
        page.add_phone_number()


    def add_email_id(self, client):
        page = uberpage(client.driver)
        page.add_email_id()

    def add_first_name(self,client):
        page = uberpage(client.driver)
        page.add_first_name()

    def add_last_name(self,client):
        page = uberpage(client.driver)
        page.add_last_name()

    def submit_add_driver(self, client):

        page = uberpage(client.driver)
        page.submit_add_driver()











