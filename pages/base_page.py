from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from utilities.screenshot_util import ScreenshotUtil



class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # def click(self, locator):
    #     WebDriverWait(self.driver, 10).until(
    #         EC.element_to_be_clickable(locator)
    #     ).click()

    # def enter_text(self, locator, text):
    #     element = WebDriverWait(self.driver, 10).until(
    #         EC.visibility_of_element_located(locator)
    #     )
    #
    #     element.clear()
    #     element.send_keys(text)

    def get_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url

    def switch_to_new_tab(self):
        self.driver.switch_to.window(
            self.driver.window_handles[-1]
        )

    def select_dropdown_by_text(self, locator, text):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )

        Select(element).select_by_visible_text(text)

    def get_text(self, locator):

        text = WebDriverWait(
            self.driver,
            10
        ).until(
            EC.visibility_of_element_located(locator)
        ).text


        print(f"Captured Text : {text}")

        return text


    def click(self, locator):

        try:

            WebDriverWait(
                self.driver,
                10
            ).until(
                EC.element_to_be_clickable(locator)
            ).click()

        except Exception as e:

            ScreenshotUtil.capture(
                self.driver,
                "click_failure"
            )

            raise Exception(
                f"Unable to click locator {locator}. "
                f"Error: {str(e)}"
            )

    def enter_text(self, locator, text):

            try:

                element = WebDriverWait(
                    self.driver,
                    10
                ).until(
                    EC.visibility_of_element_located(locator)
                )

                element.clear()
                element.send_keys(text)

            except Exception as e:

                ScreenshotUtil.capture(
                    self.driver,
                    "enter_text_failure"
                )

                raise Exception(
                    f"Unable to enter text into "
                    f"{locator}. Error: {str(e)}"
                )

    def is_displayed(self, locator):

        try:

            element = WebDriverWait(
                self.driver,
                10
            ).until(
                EC.visibility_of_element_located(locator)
            )

            return element.is_displayed()

        except Exception as e:

            ScreenshotUtil.capture(
                self.driver,
                "is_displayed_failure"
            )

            raise Exception(
                f"Unable to verify visibility of "
                f"{locator}. Error: {str(e)}"
            )