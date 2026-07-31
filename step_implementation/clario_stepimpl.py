from pages.clario_pages.clario_page import ClarioPage
from pages.uber_pages.uber_page import uberpage
from config.config_reader import ConfigReader
from utilities import client
from utilities.json_reader import JsonReader

class ClarioertStepImpl():

    def launch_application(self, client):
        client.driver.get(
            ConfigReader.get_clario_url())


    def click_on_create_account(self, client):

        create_acc = ClarioPage(client.driver)
        create_acc.create_account()

    # def enter_email(self, client, email):
    #     page = ClarioPage(client.driver)
    #     page.enter_email(email)

    def enter_email(self, client):

        data = JsonReader.get_data(
            "create_account.json",
            "valid_user"
        )

        page = ClarioPage(client.driver)

        page.enter_email(
            data["email"]
        )

    def enter_confirm_email(self, client):

        data = JsonReader.get_data(
            "create_account.json",
            "valid_user"
        )

        page = ClarioPage(client.driver)

        page.enter_confirm_email(
            data["confirm_email"]
        )

    def enter_first_name(self, client):

        data = JsonReader.get_data(
            "create_account.json",
            "valid_user"
        )

        page = ClarioPage(client.driver)

        page.enter_first_name(
            data["first_name"]
        )

    def enter_last_name(self, client):

        data = JsonReader.get_data(
            "create_account.json",
            "valid_user"
        )

        page = ClarioPage(client.driver)

        page.enter_last_name(
            data["last_name"]
        )

    def enter_password(self, client):

        data = JsonReader.get_data(
            "create_account.json",
            "valid_user"
        )

        page = ClarioPage(client.driver)

        page.enter_password(
            data["password"]
        )

    def enter_confirm_password(self, client):

        data = JsonReader.get_data(
            "create_account.json",
            "valid_user"
        )

        page = ClarioPage(client.driver)

        page.enter_confirm_password(
            data["confirm_password"]
        )
