from selenium.webdriver.common.by import By


class UberSupplierLocator:

    EMAIL = (By.XPATH, "//input[@id='PHONE_NUMBER_or_EMAIL_ADDRESS']")
    SUBMIT = (By.XPATH, "//button[@id='forward-button']")
    MORE_OPTIONS = (By.XPATH, "//button[@id='alt-action-help-v2']")
    CLICK_PASSWORD_OPTION = (By.XPATH, "//button[@id='alt-more-options-modal-password']")
    PASSWORD = (By.XPATH, "//input[@id='PASSWORD']")
    NEXT = (By.XPATH, "//button[@id='forward-button']")
    # VEHICLES_BETA = (By.XPATH, "(//span[normalize-space()='Vehicles (Beta)'])[2]")
    VEHICLES_BETA = (By.XPATH, "//span[normalize-space()='Vehicles (Beta)']")
    FILTER = (By.XPATH, "//div[@data-testid='filter-icon']")
    FILTER_CHECKBOXES = (By.XPATH, "//span[@class='_css-lhNqTx']")
    CLICK_APPLY = (By.XPATH, "//button[@class='_css-cByeRv']")
    # ADD_VEHICLE = (By.XPATH, "//button[@id='bui12__anchor']")
    ADD_VEHICLE = (By.XPATH, "//button[@data-testid='add-vehicle-btn']")
    ADD_VEHICLE_NAME = (By.XPATH, "//input[@placeholder='Ex. 2RMA345']")
    ADD_OPTIONAL_ID = (By.XPATH, "//input[@placeholder='Ex. 1234-ABCD']")
    ADD_DOCUMENT = (By.XPATH, "//div[contains(@data-tracking-payload,'Vehicle Registration')]//input[@type='file']")
    CLICK_SUBMIT_BUTTON = (By.XPATH, "//button[@data-testid='submit-vehicle-button']")
    VEHICLE_ADDED = (By.XPATH, "//div[text()='PROD']")
    TICKETS = (By.XPATH, "//span[text()= 'Tickets']")
    NEW_TICKET = (By.XPATH, "//button[@data-testid='new-ticket-button']")
    SELECT_VEHICLE = (By.XPATH, "//div[text()= 'Select vehicle']")
    TEST1 = (By.XPATH, "//li[normalize-space()='TEST1']")
    SELECT_ISSUE_TYPE = (By.XPATH, "//div[text()='Select issue type']")
    LOST_ITEM = (By.XPATH, "//li[normalize-space()='Lost item essential']")
    DESCRIPTION = (By.XPATH, "//textarea[@type='textarea']")
    SUBMIT_AND_CLAIM = (By.XPATH, "//button[text()= 'Submit & Claim']")
    TOASTER = (By.XPATH, "//div[@data-baseweb='toaster']")
    DRIVER = (By.XPATH, "//span[@data-testid='header-nav-/drivers']")
    ADD_DRIVER = (By.XPATH, "//button[@data-testid='add-driver-button']")
    # ADD_DRIVER = (By.XPATH, "//button[text()='Add driver']")

    ADD_PHONE_NUMBER = (By.XPATH, "//input[@aria-label='phone-input']")
    ADD_EMAIL_ID = (By.XPATH, "//input[@aria-label='email-input']")
    FIRST_NAME = (By.XPATH, "//input[@aria-label='first-name-input']")
    LAST_NAME = (By.XPATH, "//input[@aria-label='last-name-input']")
    ADD_NEW_DRIVER = (By.XPATH, "//button[@aria-label='Add driver']")








