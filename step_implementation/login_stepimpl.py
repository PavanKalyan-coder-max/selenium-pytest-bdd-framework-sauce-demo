from config.config_reader import ConfigReader
from pages.login_page import LoginPage


class LoginStepImpl:

    def launch_application(self, client):
        client.driver.get(
            ConfigReader.get_url()
        )

    # def login_to_application(self, client):
    #
    #     login_page = LoginPage(client.driver)
    #
    #     login_page.login(
    #         ConfigReader.get_username(),
    #         ConfigReader.get_password()
    #     )

    def login_to_application(
            self,
            client,
            username,
            password
    ):
        login_page = LoginPage(
            client.driver
        )

        login_page.login(
            username,
            password
        )

    def verify_inventory_page(self, client):

        assert "inventory" in client.driver.current_url