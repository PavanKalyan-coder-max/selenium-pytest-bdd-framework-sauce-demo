from selenium.webdriver.common.by import By


class Herokulocators:

    ALERTS = (By.XPATH, "//a[@href='/javascript_alerts']")
    CLICK_ON_JS_ALERT = (By.XPATH, "//button[@onclick='jsAlert()']")
    DROPDOWN = (By.XPATH, "//a[@href='/dropdown']")
    CLICK_DROPDOWN = (By.XPATH, "//select[@id='dropdown']")
    FILE_UPLOAD = (By.XPATH, "//a[@href='/upload']")

    FILE_UPLOADS = (By.XPATH, "//input[@id='file-upload']")
    UPLOAD_BUTTON = (By.XPATH, "//input[@id='file-submit']")
    TITLE = (By.XPATH, "//h1[@class='heading']")
    DRAG_AND_DROP = (By.XPATH, "//a[text()='Drag and Drop']")
    SOURCE_CODE = (By.XPATH, "//div[@id='column-a']")
    TARGET_CODE = (By.XPATH, "//div[@id='column-b']")
    FRAMES = (By.XPATH, "//a[text()='Frames']")
    IFRAMES = (By.XPATH, "//a[text()='iFrame']")





