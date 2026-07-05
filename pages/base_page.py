from selenium.webdriver import ActionChains
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

    def clear_text(self, locator):

        try:

            element = WebDriverWait(
                self.driver,
                10
            ).until(
                EC.visibility_of_element_located(locator)
            )

            element.clear()

        except Exception as e:

            ScreenshotUtil.capture(
                self.driver,
                "clear_text_failure"
            )

            raise Exception(
                f"Unable to clear text from "
                f"{locator}. Error: {str(e)}"
            )

    def wait_for_element_visible(self, locator):

        try:

            return WebDriverWait(
                self.driver,
                10
            ).until(
                EC.visibility_of_element_located(locator)
            )

        except Exception as e:

            ScreenshotUtil.capture(
                self.driver,
                "wait_visible_failure"
            )

            raise Exception(
                f"Element not visible: {locator}. "
                f"Error: {str(e)}"
            )

    def wait_for_element_clickable(self, locator):

        try:

            return WebDriverWait(
                self.driver,
                10
            ).until(
                EC.element_to_be_clickable(locator)
            )

        except Exception as e:

            ScreenshotUtil.capture(
                self.driver,
                "wait_clickable_failure"
            )

            raise Exception(
                f"Element not clickable: {locator}. "
                f"Error: {str(e)}"
            )

    def hover(self, locator):

        try:

            element = WebDriverWait(
                self.driver,
                10
            ).until(
                EC.visibility_of_element_located(locator)
            )

            ActionChains(
                self.driver
            ).move_to_element(
                element
            ).perform()

        except Exception as e:

            ScreenshotUtil.capture(
                self.driver,
                "hover_failure"
            )

            raise Exception(
                f"Unable to hover on "
                f"{locator}. Error: {str(e)}"
            )

    def double_click(self, locator):

        try:

            element = WebDriverWait(
                self.driver,
                10
            ).until(
                EC.element_to_be_clickable(locator)
            )

            ActionChains(
                self.driver
            ).double_click(
                element
            ).perform()

        except Exception as e:

            ScreenshotUtil.capture(
                self.driver,
                "double_click_failure"
            )

            raise Exception(
                f"Unable to double click "
                f"{locator}. Error: {str(e)}"
            )

    def take_screenshot(self, file_name):

        try:

            ScreenshotUtil.capture(
                self.driver,
                file_name
            )

        except Exception as e:

            raise Exception(
                f"Unable to capture screenshot. "
                f"Error: {str(e)}"
            )

    def click_multiple(self, *locators):

        """
        Click multiple elements one after another.
        """

        for locator in locators:
            self.click(locator)

    def accept_alert(self):
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        self.driver.switch_to.alert.dismiss()

    def get_alert_text(self):
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        return self.driver.switch_to.alert.text

    def upload_file(self, locator, file_path):
        self.driver.find_element(*locator).send_keys(file_path)