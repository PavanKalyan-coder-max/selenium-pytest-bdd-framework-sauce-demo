from selenium.webdriver import Keys
from pages.base_page import BasePage
# from locators.heroku import heroku_locators
from locators.heroku.heroku_locators import Herokulocators



class HerokuPages(BasePage):

    def heroku_page_alert(self):

        self.click(Herokulocators.ALERTS)


    def click_on_js_alert(self):

         self.click(Herokulocators.CLICK_ON_JS_ALERT)

    def accept_js_alert(self):
        self.accept_alert()

    def dismiss_js_alert(self):
        self.dismiss_alert()

    def click_dropdown_link(self):
        self.click(Herokulocators.DROPDOWN)

    # def click_dropdown_box(self):
    #     self.click(Herokulocators.CLICK_DROPDOWN)

    def select_dropdown(self, option):
        self.select_dropdown_by_text(
            Herokulocators.CLICK_DROPDOWN,
            option
        )

    def file_upload(self):

        self.click(Herokulocators.FILE_UPLOAD)

    def choose_file(self, file_path):
        self.upload_file(
            Herokulocators.FILE_UPLOADS,
            file_path
        )

    def click_upload(self):
        self.click(
            Herokulocators.UPLOAD_BUTTON
        )



