from pages.back_home_page import BackHomePage


class BackhomeStepImpl:

    def click_back_home(self, client):

        back_home_page = BackHomePage(client.driver)

        back_home_page.click_back_home()



