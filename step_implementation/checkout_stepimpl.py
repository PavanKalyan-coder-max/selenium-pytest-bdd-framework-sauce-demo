from pages.checkout_page import CheckoutPage


class CheckoutStepImpl:

    def enter_checkout_information(self, client):

        checkout_page = CheckoutPage(
            client.driver
        )

        checkout_page.fill_checkout_information(
            "Pavan",
            "Kalyan",
            "500001"
        )

    def click_finish(self, client):

        checkout_page = CheckoutPage(
            client.driver
        )

        checkout_page.click_finish()

    def verify_order_completion(self, client):

        assert "checkout-complete" in client.driver.current_url