from pages.sauce_labs_fleece_jacket_page import saucelabsfleecejacketpage


class SaucelabsfleecejacketStepImpl:

    def add_sauce_labs_fleece_jacket(self, client):

        add_sauce_labs_fleece_jacket_page = saucelabsfleecejacketpage(client.driver)

        add_sauce_labs_fleece_jacket_page.add_sauce_labs_fleece_jacket()