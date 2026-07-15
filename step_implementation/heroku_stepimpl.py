from pages.heroku_pages.heroku_page import HerokuPages
from config.config_reader import ConfigReader


class herokustepimpl:

    def launch_application(self, client):
        client.driver.get(
            ConfigReader.get_heroku_url()
        )

    def heroku_click_alert(self, client):

        heroku_click_on_alert = HerokuPages(client.driver)
        heroku_click_on_alert.heroku_page_alert()


    def click_on_JS_alerts_step(self, client):

        clicking_on_JS_alert = HerokuPages(client.driver)
        clicking_on_JS_alert.click_on_js_alert()

    def accept_alert(self, client):

        accept_alert_page = HerokuPages(client.driver)
        accept_alert_page.accept_js_alert()

    def dismiss_alert(self, client):

        dismiss_alert_page = HerokuPages(client.driver)
        dismiss_alert_page.dismiss_js_alert()

    def go_to_home_page(self, client):
        client.driver.get("https://the-internet.herokuapp.com/")


    def click_dropdown_link(self, client):
        clicking_dropdown_link = HerokuPages(client.driver)
        clicking_dropdown_link.click_dropdown_link()


    # def click_dropdown_box(self, client):
    #
    #     clicking_dropdown_box = HerokuPages(client.driver)
    #     clicking_dropdown_box.click_dropdown_box()

    def select_dropdown_step(self, client, option):
        dropdown = HerokuPages(client.driver)
        dropdown.select_dropdown(option)



    def click_file_upload(self, client):
        file = HerokuPages(client.driver)
        file.file_upload()

    def upload_file_step(self, client, file_path):

        uploading_files = HerokuPages(client.driver)
        uploading_files.choose_file(file_path)
        uploading_files.click_upload()


    def get_page_title(self, client):
        get_the_page_title = HerokuPages(client.driver)
        get_the_page_title.page_title()

    def current_url(self, client):

        get_current_url = HerokuPages(client.driver)
        get_current_url.current_url()

    def verify_current_url(self, client):
        verified_current_url = HerokuPages(client.driver)
        verified_current_url.verify_current_url()





















