from pages.base_page import BasePage

class DemoPage(BasePage):

    def click(self, locator, description="Element"):
        print("Executing click from DemoPage")

        super().click(locator, description)  # Reuse BasePage's click method