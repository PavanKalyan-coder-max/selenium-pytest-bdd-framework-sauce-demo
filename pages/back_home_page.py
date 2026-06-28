from pages.base_page import BasePage
from locators.back_home_locator import BackhomeLocators


class BackHomePage(BasePage):

    def click_back_home(self):

        self.click(BackhomeLocators.BACK_HOME_BUTTON)



