from pages.uber_pages.uber_page import uberpage
from config.config_reader import ConfigReader

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
