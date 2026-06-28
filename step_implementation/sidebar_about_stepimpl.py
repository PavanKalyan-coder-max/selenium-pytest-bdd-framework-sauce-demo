from pages.about_page import Sidebaraboutpage


class Sidebaraboutstepimpl:

     def click_sidebar_about(self, client):

         clicking_sidebar_about = Sidebaraboutpage(client.driver)
         clicking_sidebar_about.click_sidebar_about()


     def click_book_a_demo(self, client):

         clicking_book_a_demo = Sidebaraboutpage(client.driver)
         clicking_book_a_demo.click_book_a_demo_page()


     def enter_text_business_mail(self, client):
          print(client.driver.current_url)

          enter_text_business_mail_name = Sidebaraboutpage(client.driver)
          enter_text_business_mail_name.enter_business_email("spavan85685@gmail.com")

     def enter_text_company_name(self, client):

         entering_text_company_name = Sidebaraboutpage(client.driver)
         entering_text_company_name.enter_company_name("INDIUM SOFTWARE")


     def enter_comments_text_free(self, client):

         entering_comments_text = Sidebaraboutpage(client.driver)
         entering_comments_text.enter_comments_text("HI PAVAN HERE")

     def enter_first_name_impl(self, client):
         entering_first_name = Sidebaraboutpage(client.driver)
         entering_first_name.enter_first_name("Pavan Kalyan")

     def enter_last_name_impl(self, client):
         entering_last_name = Sidebaraboutpage(client.driver)
         entering_last_name.enter_last_name("Sonta")


     def enter_phone_number_impl(self, client):

         entering_phone_number = Sidebaraboutpage(client.driver)
         entering_phone_number.enter_phone_number("9491426192")

     def select_drop_down_by_text(self, client):

         selecting_drop_down = Sidebaraboutpage(client.driver)
         selecting_drop_down.select_dropdown("India")

     def select_interests_dropdown(self, client):

         selecting_drop_down = Sidebaraboutpage(client.driver)
         selecting_drop_down.select_interests("Sauce AI Agents")


     def select_check_box(self, client):

         selecting_check_box = Sidebaraboutpage(client.driver)
         selecting_check_box.select_checkbox()


     def click_submit(self,client):

         clicking_submit_button = Sidebaraboutpage(client.driver)
         clicking_submit_button.click_submit_button()


     def click_logout(self, client):

         clicking_logout_button = Sidebaraboutpage(client.driver)
         clicking_logout_button.click_logout_button()

     def products_button(self, client):

         clicking_products_button_link = Sidebaraboutpage(client.driver)
         clicking_products_button_link.products_link_button()

     def verify_get_text(self, client):

         verifying_get_text = Sidebaraboutpage(client.driver)
         verifying_get_text.verify_text()




