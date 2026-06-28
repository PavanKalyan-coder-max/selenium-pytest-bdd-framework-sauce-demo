from selenium.webdriver.common.by import By


class InventoryLocators:

    ADD_BACKPACK = (
        By.ID,
        "add-to-cart-sauce-labs-backpack"
    )

    CART_ICON = (
        By.CLASS_NAME,
        "shopping_cart_link"
    )