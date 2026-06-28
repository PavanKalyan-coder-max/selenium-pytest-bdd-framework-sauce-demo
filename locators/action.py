from selenium.webdriver.common.by import By

class Sidebaraboutlocator:

    SIDEBAR_ABOUT = (
        By.XPATH, "//a[@id='about_sidebar_link']"

    )

    BOOK_A_DEMO = (By.XPATH, "//button[text()='Book a demo']")

    BUSINESS_MAIL = (By.XPATH, "//input[@name='Email']")
    COMPANY_NAME = (By.XPATH, "//input[@name='Company']")
    COMMENTS_TEXT = (By.XPATH, "//textarea[@id='Sales_Contact_Comments__c']")
    FIRST_NAME = (By.XPATH, "//input[@id='FirstName']")
    LAST_NAME = (By.XPATH, "//input[@id='LastName']")
    PHONE_NUMBER = (By.XPATH, "//input[@id='Phone']")

    SELECT_DROPDOWN = (By.XPATH, "//select[@id='Country']")
    SELECT_INTERESTS = (By.XPATH, "//select[@id='Solution_Interest__c']")
    SELECT_CHECKBOX = (By.XPATH, "//label[@id='LblmktoCheckbox_47937_0']")
    CLICK_SUBMIT = (By.XPATH, "//button[@class='mktoButton']")
    LOGOUT_BUTTON = (By.XPATH, "//a[@id='logout_sidebar_link']")
    PRODUCTS_LINK = (By.XPATH, "//div[@role='region']//a[@href='/products']//span[normalize-space()='Platform for Test']")
    GET_MESSAGE = (By.XPATH, "//span[text()='Built on the Sauce Labs enterprise-grade platform, trusted by thousands of global brands']")


















