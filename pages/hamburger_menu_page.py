from pages.base_page import BasePage
from locators.hamburger_menu_locator import HamburgerMenuLocator


class HamburgerMenuPage(BasePage):
    def click_hamburger_menu(self):
        self.click(HamburgerMenuLocator.HamburgerMenu)


