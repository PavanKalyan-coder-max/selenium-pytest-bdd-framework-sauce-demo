from pages.base_page import BasePage

from locators.sauce_labs_fleece_jacket_locator import saucelabslocators


class saucelabsfleecejacketpage(BasePage):

    def add_sauce_labs_fleece_jacket(self):

        self.click(saucelabslocators.FLEECE_JACKET)



