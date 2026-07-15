from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class BrowserFactory:

    @staticmethod
    def get_driver(browser):

        browser = browser.lower()

        if browser == "chrome":

            options = webdriver.ChromeOptions()

            prefs = {
                "credentials_enable_service": False,
                "profile.password_manager_enabled": False
            }

            options.add_experimental_option("prefs", prefs)
            options.add_argument("--disable-save-password-bubble")
            options.add_argument("--disable-features=PasswordCheck")
            options.add_argument("--disable-password-generation")
            options.add_argument("--guest")

            driver = webdriver.Chrome(
                service=Service(
                    ChromeDriverManager().install()
                ),
                options=options
            )

            return driver

        elif browser == "edge":

            options = webdriver.EdgeOptions()

            driver = webdriver.Edge(
                service=EdgeService(
                    EdgeChromiumDriverManager().install()
                ),
                options=options
            )

            return driver

        elif browser == "firefox":

            options = webdriver.FirefoxOptions()

            driver = webdriver.Firefox(
                service=FirefoxService(
                    GeckoDriverManager().install()
                ),
                options=options
            )

            return driver



        else:
            raise ValueError(f"Unsupported Browser : {browser}")