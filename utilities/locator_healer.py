from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class LocatorHealer:

    @staticmethod
    def find_element(driver, locators, timeout=5):

        for locator in locators:

            try:

                print(f"Trying locator: {locator}")

                element = WebDriverWait(driver, timeout).until(
                    EC.presence_of_element_located(locator)
                )

                print(f"Success: {locator}")

                return element

            except TimeoutException:

                print(f"Failed: {locator}")

                continue

        raise Exception("All locator strategies failed.")