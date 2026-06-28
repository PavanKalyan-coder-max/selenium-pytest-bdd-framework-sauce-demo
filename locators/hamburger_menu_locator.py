from selenium.webdriver.common.by import By

class HamburgerMenuLocator:

    HamburgerMenu = (
        By.XPATH, "//button[@id='react-burger-menu-btn']"
    )