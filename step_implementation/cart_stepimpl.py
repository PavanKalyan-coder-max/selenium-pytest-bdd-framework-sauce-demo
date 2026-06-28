from pages.cart_page import CartPage


class CartStepImpl:

    def click_checkout(self, client):

        cart_page = CartPage(
            client.driver
        )

        cart_page.click_checkout()

    def verify_checkout_information_page(self, client):

        assert "checkout-step-one" in client.driver.current_url