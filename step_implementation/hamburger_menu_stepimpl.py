from pages.back_home_page import BackHomePage
from pages.hamburger_menu_page import HamburgerMenuPage


class HamburgerMenuStepImpl:
    def click_on_hamburger_menu(self, client):

        clicking_hamburger_menu = HamburgerMenuPage(client.driver)

        clicking_hamburger_menu.click_hamburger_menu()

