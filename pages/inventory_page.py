from pages.base_page import BasePage

from locators.inventory_locators import InventoryLocators


class InventoryPage(BasePage):

    def add_backpack_to_cart(self):

        self.click(
            InventoryLocators.ADD_BACKPACK
        )

    def open_cart(self):

        self.click(
            InventoryLocators.CART_ICON
        )