from selenium.webdriver.common.by import By


class UberSupplierLocator:

    EMAIL = (By.XPATH, "//input[@id='PHONE_NUMBER_or_EMAIL_ADDRESS']")
    SUBMIT = (By.XPATH, "//button[@id='forward-button']")
    MORE_OPTIONS = (By.XPATH, "//button[@id='alt-action-help-v2']")
    CLICK_PASSWORD_OPTION = (By.XPATH, "//button[@id='alt-more-options-modal-password']")
    PASSWORD = (By.XPATH, "//input[@id='PASSWORD']")
    NEXT = (By.XPATH, "//button[@id='forward-button']")
    VEHICLES_BETA = (By.XPATH, "(//span[normalize-space()='Vehicles (Beta)'])[2]")





