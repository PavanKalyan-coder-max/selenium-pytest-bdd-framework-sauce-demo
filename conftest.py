"""from utilities.client import Client
from step_implementation.login_stepimpl import LoginStepImpl
from step_implementation.inventory_stepimpl import InventoryStepImpl
from step_implementation.cart_stepimpl import CartStepImpl
from step_implementation.checkout_stepimpl import CheckoutStepImpl
from step_implementation.back_home_stepimpl import BackhomeStepImpl
from step_implementation.sauce_labs_fleece_jacket_stepimpl import SaucelabsfleecejacketStepImpl
from step_implementation.hamburger_menu_stepimpl import HamburgerMenuStepImpl
from step_implementation.sidebar_about_stepimpl import Sidebaraboutstepimpl
import json
from datetime import datetime

import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from config.config_reader import ConfigReader
from config.config_reader import ENV

print(f"Running in Environment: {ENV}")

from utilities.client import Client
from step_implementation.login_stepimpl import LoginStepImpl

CURRENT_DRIVER = None


def write_test_result(result_data):

    output_file = "reports/output.json"

    try:
        with open(output_file, "r") as file:
            data = json.load(file)
    except:
        data = []

    data.append(result_data)

    with open(output_file, "w") as file:
        json.dump(data, file, indent=4)


@pytest.fixture(scope="function")
def client():
    global CURRENT_DRIVER

    obj = Client()

    obj.driver = webdriver.Chrome(
        service=Service(
            ChromeDriverManager().install()
        )
    )

    CURRENT_DRIVER = obj.driver

    print(f"DRIVER STORED = {CURRENT_DRIVER}")

    obj.driver.maximize_window()

    obj.login_stepimpl = LoginStepImpl()
    obj.inventory_stepimpl = InventoryStepImpl()
    obj.cart_stepimpl = CartStepImpl()
    obj.checkout_stepimpl = CheckoutStepImpl()
    obj.back_home_stepimpl = BackhomeStepImpl()
    obj.sauce_labs_fleece_jacket_stepimpl = SaucelabsfleecejacketStepImpl()
    obj.hamburger_menu_stepimpl = HamburgerMenuStepImpl()
    obj.sidebar_about_stepimpl = Sidebaraboutstepimpl()

    yield obj


    obj.driver.quit()

    CURRENT_DRIVER = None


# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#
#     outcome = yield
#     report = outcome.get_result()
#
#     if report.when == "call":
#
#         if report.failed:
#
#             print(f"Test Failed : {item.name}")


import os
from datetime import datetime
import pytest


import os
from datetime import datetime
import pytest


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()


    if report.when == "call":


        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        if report.passed:


            folder = os.path.join(
                "reports",
                "screenshots",
                "passed"
            )

            os.makedirs(folder, exist_ok=True)

            screenshot_path = os.path.join(
                folder,
                f"{item.name}_{timestamp}.png"
            )

            print(f"Screenshot path = {screenshot_path}")

            if CURRENT_DRIVER:
                result = CURRENT_DRIVER.save_screenshot(screenshot_path)

            result = {
                "test_name": item.name,
                "status": "PASS",
                "execution_time": round(report.duration, 2),
                "execution_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "screenshot": screenshot_path
            }

            write_test_result(result)


        elif report.failed:

            print("REPORT FAILED")

            result = {
                "test_name": item.name,
                "status": "FAIL",
                "execution_time": round(report.duration, 2),
                "execution_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "screenshot": screenshot_path
            }

            write_test_result(result)

            """


from utilities.client import Client

from step_implementation.login_stepimpl import LoginStepImpl
from step_implementation.inventory_stepimpl import InventoryStepImpl
from step_implementation.cart_stepimpl import CartStepImpl
from step_implementation.checkout_stepimpl import CheckoutStepImpl
from step_implementation.back_home_stepimpl import BackhomeStepImpl
from step_implementation.sauce_labs_fleece_jacket_stepimpl import SaucelabsfleecejacketStepImpl
from step_implementation.hamburger_menu_stepimpl import HamburgerMenuStepImpl
from step_implementation.sidebar_about_stepimpl import Sidebaraboutstepimpl

import os
import json
import pytest

from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from config.config_reader import ENV

print(f"Running in Environment: {ENV}")

CURRENT_DRIVER = None


# ============================================================
# RESET REPORT DATA BEFORE EXECUTION
# ============================================================

def pytest_sessionstart(session):
    os.makedirs("reports", exist_ok=True)

    with open("reports/output.json", "w") as file:
        json.dump([], file)


# ============================================================
# WRITE TEST RESULT TO JSON
# ============================================================

def write_test_result(result_data):

    output_file = "reports/output.json"

    try:
        with open(output_file, "r") as file:
            data = json.load(file)

    except Exception:
        data = []

    data.append(result_data)

    with open(output_file, "w") as file:
        json.dump(data, file, indent=4)


# ============================================================
# CLIENT FIXTURE
# ============================================================

# @pytest.fixture(scope="function")
# def client():
#
#     global CURRENT_DRIVER
#
#     obj = Client()
#
#     obj.driver = webdriver.Chrome(
#         service=Service(
#             ChromeDriverManager().install()
#         )
#     )
#
#     CURRENT_DRIVER = obj.driver
#
#     obj.driver.maximize_window()
#
#     obj.login_stepimpl = LoginStepImpl()
#     obj.inventory_stepimpl = InventoryStepImpl()
#     obj.cart_stepimpl = CartStepImpl()
#     obj.checkout_stepimpl = CheckoutStepImpl()
#     obj.back_home_stepimpl = BackhomeStepImpl()
#     obj.sauce_labs_fleece_jacket_stepimpl = SaucelabsfleecejacketStepImpl()
#     obj.hamburger_menu_stepimpl = HamburgerMenuStepImpl()
#     obj.sidebar_about_stepimpl = Sidebaraboutstepimpl()
#
#     yield obj
#
#     obj.driver.quit()
#
#     CURRENT_DRIVER = None
# ==================================================================================================
# New crome code

CURRENT_DRIVER = None


@pytest.fixture(scope="function")
def client():

    global CURRENT_DRIVER

    obj = Client()

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

    obj.driver = webdriver.Chrome(
        service=Service(
            ChromeDriverManager().install()
        ),
        options=options
    )

    CURRENT_DRIVER = obj.driver

    obj.driver.maximize_window()

    obj.login_stepimpl = LoginStepImpl()
    obj.inventory_stepimpl = InventoryStepImpl()
    obj.cart_stepimpl = CartStepImpl()
    obj.checkout_stepimpl = CheckoutStepImpl()
    obj.back_home_stepimpl = BackhomeStepImpl()
    obj.sauce_labs_fleece_jacket_stepimpl = SaucelabsfleecejacketStepImpl()
    obj.hamburger_menu_stepimpl = HamburgerMenuStepImpl()
    obj.sidebar_about_stepimpl = Sidebaraboutstepimpl()

    yield obj

    obj.driver.quit()

    CURRENT_DRIVER = None
# ============================================================
# SCREENSHOT + REPORT HOOK
# ============================================================

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when != "call":
        return

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # ========================================================
    # PASS
    # ========================================================

    if report.passed:

        folder = os.path.join(
            "reports",
            "screenshots",
            "passed"
        )

        os.makedirs(folder, exist_ok=True)

        screenshot_path = os.path.join(
            folder,
            f"{item.name}_{timestamp}.png"
        )

        if CURRENT_DRIVER:
            CURRENT_DRIVER.save_screenshot(screenshot_path)

        print(f"PASS Screenshot Saved: {screenshot_path}")

        test_result = {
            "test_name": item.name,
            "status": "PASS",
            "execution_time": round(report.duration, 2),
            "execution_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "screenshot": screenshot_path
        }

        write_test_result(test_result)

    # ========================================================
    # FAIL
    # ========================================================

    elif report.failed:

        folder = os.path.join(
            "reports",
            "screenshots",
            "failed"
        )

        os.makedirs(folder, exist_ok=True)

        screenshot_path = os.path.join(
            folder,
            f"{item.name}_{timestamp}.png"
        )

        if CURRENT_DRIVER:
            CURRENT_DRIVER.save_screenshot(screenshot_path)

        print(f"FAIL Screenshot Saved: {screenshot_path}")

        test_result = {
            "test_name": item.name,
            "status": "FAIL",
            "execution_time": round(report.duration, 2),
            "execution_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "screenshot": screenshot_path
        }

        write_test_result(test_result)

    import subprocess

    def pytest_sessionfinish(session, exitstatus):

        print("\nGenerating HTML Report...")

        subprocess.run(
            ["python", "reports/customreport/parser.py"],
            check=False
        )

        print("HTML Report Generated Successfully")


import subprocess
import webbrowser
import os


def pytest_sessionfinish(session, exitstatus):

    print("\nSESSION FINISH HOOK EXECUTED")

    result = subprocess.run(
        ["python", "reports/customreport/parser.py"],
        capture_output=True,
        text=True
    )

    print("STDOUT:")
    print(result.stdout)

    print("STDERR:")
    print(result.stderr)

    report_path = os.path.abspath(
        "reports/customreport/report.html"
    )

    webbrowser.open(
        f"file:///{report_path.replace(os.sep, '/')}"
    )

    print("REPORT OPENED IN BROWSER")