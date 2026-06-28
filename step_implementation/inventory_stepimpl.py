from pages.inventory_page import InventoryPage


class InventoryStepImpl:

    def add_product_to_cart(self, client):

        inventory_page = InventoryPage(
            client.driver
        )

        inventory_page.add_backpack_to_cart()

    def open_cart(self, client):

        inventory_page = InventoryPage(
            client.driver
        )

        inventory_page.open_cart()

    def verify_cart_page(self, client):

        assert "cart" in client.driver.current_url