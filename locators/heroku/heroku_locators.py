from selenium.webdriver.common.by import By


class Herokulocators:

    ALERTS = (By.XPATH, "//a[@href='/javascript_alerts']")
    CLICK_ON_JS_ALERT = (By.XPATH, "//button[@onclick='jsAlert()']")
    DROPDOWN = (By.XPATH, "//a[@href='/dropdown']")
    CLICK_DROPDOWN = (By.XPATH, "//select[@id='dropdown']")
    FILE_UPLOAD = (By.XPATH, "//a[@href='/upload']")

    FILE_UPLOADS = (By.XPATH, "//input[@id='file-upload']")
    UPLOAD_BUTTON = (By.XPATH, "//input[@id='file-submit']")





