from selenium.webdriver import Keys

from pages.base_page import BasePage
from locators.action import Sidebaraboutlocator

class Sidebaraboutpage(BasePage):

     def click_sidebar_about(self):

         self.click(Sidebaraboutlocator.SIDEBAR_ABOUT)


     def click_book_a_demo_page(self):

          self.click(Sidebaraboutlocator.BOOK_A_DEMO)
          self.switch_to_new_tab()

     def enter_business_email(self, email):

          self.enter_text(Sidebaraboutlocator.BUSINESS_MAIL, email)


     def enter_company_name(self, company_name):

          self.enter_text(Sidebaraboutlocator.COMPANY_NAME, company_name)

     def enter_comments_text(self, text):

          self.enter_text(Sidebaraboutlocator.COMMENTS_TEXT, text)

     def enter_first_name(self, text):

         self.enter_text(Sidebaraboutlocator.FIRST_NAME, text)

     def enter_last_name(self, text):

         self.enter_text(Sidebaraboutlocator.LAST_NAME, text)

     def enter_phone_number(self, text):

         self.enter_text(Sidebaraboutlocator.PHONE_NUMBER, text)

     def select_dropdown(self, country):

         self.select_dropdown_by_text(Sidebaraboutlocator.SELECT_DROPDOWN, country)


     def select_interests(self, text):

         self.select_dropdown_by_text(Sidebaraboutlocator.SELECT_INTERESTS, text)


     def select_checkbox(self):

         self.click(Sidebaraboutlocator.SELECT_CHECKBOX)

     def click_submit_button(self):

         self.click(Sidebaraboutlocator.CLICK_SUBMIT)

     def click_logout_button(self):

         self.click(Sidebaraboutlocator.LOGOUT_BUTTON)

     def products_link_button(self):
         self.driver.execute_script(
             "window.scrollTo(0, document.body.scrollHeight);")

         self.click(Sidebaraboutlocator.PRODUCTS_LINK)


     def verify_text(self):
         element = self.driver.find_element(*Sidebaraboutlocator.GET_MESSAGE)

         self.driver.execute_script(
             "arguments[0].scrollIntoView({block:'center'});",
             element
         )

         actual_text = self.get_text(Sidebaraboutlocator.GET_MESSAGE)

         print(f"Platform Text : {actual_text}")

         assert "Built on the Sauce Labs enterprise-grade platform" in actual_text

         print("✓ Platform text verified successfully")




     def index_disclaimer_text(self):

         actual_text = self.get_text(Sidebaraboutlocator.INDEX_DISCLAIMER)

         expected_text = "By signing in, you agree with the "

         assert expected_text in actual_text

         print("✓ Platform text verified successfully")

     def logo_visa(self):
         result = self.is_displayed(Sidebaraboutlocator.LOGO_VISA)
         print(result)




     def go_to_app_button(self):
         self.click(Sidebaraboutlocator.GO_TO_APP)


     def try_for_free_button(self):
         self.click(Sidebaraboutlocator.TRY_FOR_FREE)




