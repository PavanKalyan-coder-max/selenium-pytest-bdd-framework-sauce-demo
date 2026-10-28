
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_uber_browser_data():

    driver = webdriver.Chrome()

    try:
        # 1. Open Uber Supplier Portal
        driver.get("https://supplier.uber.com/")

        # 2. Capture browser data
        page_title = driver.title
        page_url = driver.current_url

        page_text = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(
                (By.TAG_NAME, "body")
            )
        ).text

        # 3. Variables and data types
        expected_text = "What's your phone number or email?"

        is_login_page = expected_text in page_text
        test_result = "PASS" if is_login_page else "FAIL"

        print("\n--- Uber Browser Information ---")
        print("Page Title:", page_title)
        print("Title Data Type:", type(page_title))
        print("Page URL:", page_url)
        print("URL Data Type:", type(page_url))
        print("Page Text:", page_text)
        print("Page Text Data Type:", type(page_text))
        print("Expected Text:", expected_text)
        print("Is Login Page:", is_login_page)
        print("Boolean Data Type:", type(is_login_page))
        print("Test Result:", test_result)
        print("Result Data Type:", type(test_result))

        # 4. Comparison operators
        expected_title = "Sign up or Log in with Uber"

        is_title_correct = page_title == expected_title
        print("Is Title Correct:", is_title_correct)

        wrong_title = "Uber Supplier Dashboard"
        is_title_different = page_title != wrong_title
        print("Is Title Different:", is_title_different)

        title_length = len(page_title)
        minimum_length = 10
        maximum_length = 30

        print("Title Length:", title_length)
        print(
            "Is Title Longer Than 10 Characters:",
            title_length > minimum_length
        )
        print(
            "Is Title Shorter Than 30 Characters:",
            title_length < maximum_length
        )

        minimum_title_length = 27
        maximum_title_length = 27

        print(
            "Is Title Long Enough:",
            title_length >= minimum_title_length
        )
        print(
            "Is Title Within Limit:",
            title_length <= maximum_title_length
        )

        # 5. Logical operators
        is_login_page_correct = (
            page_title == expected_title
            and expected_text in page_text
        )
        print("Is Login Page Correct:", is_login_page_correct)

        is_uber_auth_page = (
            page_title == expected_title
            or expected_text in page_text
        )
        print("Is Uber Authentication Page:", is_uber_auth_page)

        is_title_incorrect = not is_title_correct
        print("Is Title Incorrect:", is_title_incorrect)

        # 6. If/else validation
        if page_title == expected_title and expected_text in page_text:
            print("PASS: Uber login page is verified")
        else:
            print("FAIL: Uber login page verification failed")

        # 7. For loop with browser details
        browser_details = [page_title, page_url]

        for detail in browser_details:
            print("Browser Detail:", detail)

        # 8. For loop with if/else
        for detail in browser_details:
            if detail:
                print("PASS: Browser detail is available")
            else:
                print("FAIL: Browser detail is missing")

        # 9. Loop through expected webpage texts
        expected_texts = [
            "What's your phone number or email?",
            "Continue",
            "Continue with Google"
        ]

        for text in expected_texts:
            if text in page_text:
                print(f"PASS: '{text}' is displayed")
            else:
                print(f"FAIL: '{text}' is missing")

        # 10. Dictionary validation with assert
        expected_page_data = {
            "title": "Sign up or Log in with Uber",
            "login_text": "What's your phone number or email?",
            "continue_text": "Continue"
        }

        actual_page_data = {
            "title": page_title,
            "login_text": page_text,
            "continue_text": page_text
        }

        for key, expected_value in expected_page_data.items():
            actual_value = actual_page_data[key]

            if expected_value in actual_value:
                print(f"PASS: {key} verified")
            else:
                print(f"FAIL: {key} not verified")

            assert expected_value in actual_value, (
                f"{key} validation failed"
            )

    finally:
        driver.quit()
