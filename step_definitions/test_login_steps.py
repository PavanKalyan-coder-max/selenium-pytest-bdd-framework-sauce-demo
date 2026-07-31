from pytest_bdd import scenarios, given, when, then
import time
from pytest_bdd import parsers

# scenarios("../features/login.feature")
# scenarios("../features/logout.feature")
# scenarios("../features/Communication.feature")
# scenarios("../features/products.feature")
# scenarios("../features/new_account.feature")
# scenarios("../features/heroku_features/alert.feature")
# scenarios("../features/uber_feature/uber_login.feature")
scenarios("../features/clario_feature/create_account2.feature")




@given("User launches SauceDemo application")
def launch_application(client):
    client.login_stepimpl.launch_application(client)

@given("User launches heroku web application")
def launch_application(client):
    client.heroku_stepimpl.launch_application(client)


@given("User launches uber web application")
def launch_application(client):
    client.ubersupplier_stepimpl.launch_application(client)


@when("User enters valid email")
def uber_page_email(client):
    client.ubersupplier_stepimpl.uber_page_email(client)
    # client.ubersupplier_stepimpl.uber_page_email(client, "nlogan+test+avfleet@ext.uber.com")
    time.sleep(4)


@when("User enters valid uber password")
def click_on_password(client):
    # client.ubersupplier_stepimpl.click_on_password(client, "Uber12345")
    client.ubersupplier_stepimpl.click_on_password(client)
    time.sleep(4)



@when("User clicks on continue")
def uber_submit(client):
    client.ubersupplier_stepimpl.uber_submit(client)

@when("User clicks on more options")
def click_on_more_options(client):
    client.ubersupplier_stepimpl.click_on_more_options(client)


@when("User clicks on password option")
def click_on_password_option(client):
    client.ubersupplier_stepimpl.click_on_password_option(client)


@when("User clicks on next button")
def click_next(client):
    client.ubersupplier_stepimpl.click_next_button(client)
    time.sleep(4)



@when(parsers.parse('User logs in with "{username}" and "{password}"'))
def login(client, username, password):
    client.login_stepimpl.login_to_application(
        client,
        username,
        password
    )
    time.sleep(5)



@when("User adds backpack to cart")
def add_product(client):
    time.sleep(5)
    client.inventory_stepimpl.add_product_to_cart(client)


@when("User clicks cart icon")
def open_cart(client):
   # time.sleep(5)
    client.inventory_stepimpl.open_cart(client)


@then("User should be navigated to cart page")
def verify_cart_page(client):
    # time.sleep(5)
    client.inventory_stepimpl.verify_cart_page(client)


@when("User clicks checkout button")
def click_checkout(client):
    # time.sleep(5)
    client.cart_stepimpl.click_checkout(client)


@then("User should be navigated to checkout information page")
def verify_checkout_page(client):
    # time.sleep(5)
    client.cart_stepimpl.verify_checkout_information_page(client)

@when("User enters checkout information")
def enter_checkout_information(client):
    client.checkout_stepimpl.enter_checkout_information(client)


@when("User clicks finish button")
def click_finish(client):
    client.checkout_stepimpl.click_finish(client)


@then("User should see order completion page")
def verify_order_complete(client):
    # time.sleep(5)
    client.checkout_stepimpl.verify_order_completion(client)


@then("User clicks back home page")
def click_back_home(client):
    # time.sleep(5)
    print("===== BACK HOME STEP EXECUTED =====")
    client.back_home_stepimpl.click_back_home(client)


@when("User adds fleece jacket to cart")
def add_sauce_labs_fleece_jacket(client):
    # time.sleep(5)
    print("===== another item selected to cart =====")
    client.sauce_labs_fleece_jacket_stepimpl.add_sauce_labs_fleece_jacket(client)


@when("User clicks hamburgermenu")
def click_on_hamburger_menu(client):
    # time.sleep(5)
    print("===== successfully clicked on hamburger menu =====")
    client.hamburger_menu_stepimpl.click_on_hamburger_menu(client)


@when("User clicks on about")
def click_sidebar_about(client):
    client.sidebar_about_stepimpl.click_sidebar_about(client)
    time.sleep(5)


@when("User clicks on book a demo")
def click_book_a_demo(client):
    client.sidebar_about_stepimpl.click_book_a_demo(client)
    time.sleep(5)

@when("User enters business email")
def enter_text_business_mail(client):
    client.sidebar_about_stepimpl.enter_text_business_mail(client)
    time.sleep(5)

@when("User enters company name")
def enter_text_company_name(client):
    client.sidebar_about_stepimpl.enter_text_company_name(client)


@when("User comments in the free text box")
def enter_comments_text_free(client):
    client.sidebar_about_stepimpl.enter_comments_text_free(client)

@when("User enters first name")
def enter_first_name_impl(client):
    client.sidebar_about_stepimpl.enter_first_name_impl(client)

@when("User enters last name")
def enter_last_name_impl(client):
    client.sidebar_about_stepimpl.enter_last_name_impl(client)


@when("User enters phone number")
def enter_phone_number_impl(client):
    client.sidebar_about_stepimpl.enter_phone_number_impl(client)
    # time.sleep(5)

@when("User selects country")
def select_drop_down_by_text(client):
    client.sidebar_about_stepimpl.select_drop_down_by_text(client)
    # time.sleep(5)

@when("User selects interest")
def select_interests_dropdown(client):
    client.sidebar_about_stepimpl.select_interests_dropdown(client)
    # time.sleep(5)

@when("User clicks checkbox")
def select_check_box(client):
    client.sidebar_about_stepimpl.select_check_box(client)
    # time.sleep(5)

@when("User clicks on submit")
def click_submit(client):
    client.sidebar_about_stepimpl.click_submit(client)
    # time.sleep(5)

@then("User logouts the application")
def click_logout(client):
    client.sidebar_about_stepimpl.click_logout(client)


@when("User clicks on products")
def products_button(client):
    time.sleep(5)
    client.sidebar_about_stepimpl.products_button(client)

@when("User verify the text")
def verify_get_text(client):
    client.sidebar_about_stepimpl.verify_get_text(client)

@when("User clicks on go to app")
def go_to_app(client):
    client.sidebar_about_stepimpl.go_to_app(client)





@when("User clicks on try for free")
def try_for_free_button(client):
    client.sidebar_about_stepimpl.try_for_free_button(client)


@when("User verify index disclaimer text")
def index_disclaimer_text(client):
    client.sidebar_about_stepimpl.index_disclaimer_text(client)
    time.sleep(5)

@when("User verify visa logo")
def logo_visa_page(client):

    client.sidebar_about_stepimpl.logo_visa_page(client)


@when("User selects multiple products")
def click_multiple_locators(client):
    client.sidebar_about_stepimpl.click_multiple_locators(client)
    time.sleep(5)

@when("User clicks on java alerts")
def heroku_click_alert(client):
    client.heroku_stepimpl.heroku_click_alert(client)



@when("User click on JS alert")
def click_on_JS_alerts_step(client):
    client.heroku_stepimpl.click_on_JS_alerts_step(client)
    # time.sleep(4)


@when("User accept the JS alert")
def accept_alert(client):
    client.heroku_stepimpl.accept_alert(client)
    time.sleep(4)


@when("User dismiss the JS alert")
def dismiss_alert(client):
    client.heroku_stepimpl.dismiss_alert(client)
    # time.sleep(4)

@when("User navigates back to home page")
def go_to_home_page(client):
    client.heroku_stepimpl.go_to_home_page(client)


@when("User clicks on dropdown link")
def click_dropdown_link(client):
    client.heroku_stepimpl.click_dropdown_link(client)


# @when("User clicks on dropdown box")
# def click_dropdown_box(client):
#     client.heroku_stepimpl.click_dropdown_box(client)
#     time.sleep(3)


# @when('User selects "{option}" from dropdown')
# def select_dropdown(client, option):
#
#     client.heroku_stepimpl.select_dropdown_step(
#         client,
#         option
#     )



@when(parsers.parse('User selects "{option}" from dropdown'))
def select_dropdown_step(client, option):

    client.heroku_stepimpl.select_dropdown_step(
        client,
        option
    )
    time.sleep(3)


@when("User clicks file upload")
def click_file_upload(client):
    client.heroku_stepimpl.click_file_upload(client)

@when(parsers.parse('User uploads "{file_path}"'))
def upload_file_step(client, file_path):

    client.heroku_stepimpl.upload_file_step(
        client,
        file_path
    )

@when("User prints page title")
def page_title_print(client):
    client.heroku_stepimpl.get_page_title(client)
    # time.sleep(3)

@when("User prints current url")
def current_page_url(client):
    client.heroku_stepimpl.current_url(client)


@when("User verifies current url")
def verify_page_url(client):
    client.heroku_stepimpl.verify_current_url(client)



@when("User clicks on vehicles beta")
def click_vehicles_beta(client):
    client.ubersupplier_stepimpl.click_vehicles_beta(client)
    time.sleep(5)


@given("User launches ERT Clario URL")
def launch_application(client):
    client.clario_stepimpl.launch_application(client)
    time.sleep(5)

@when("User clicks on create acocunt")
def click_on_create_account(client):
    client.clario_stepimpl.click_on_create_account(client)
    time.sleep(5)

# @when('User enters Email "{email}"')
# def enter_email(client, email):
#     client.clario_stepimpl.enter_email(email)
#     time.sleep(5)


# @when(parsers.parse('User enters Email "{email}"'))
# def enter_email(client, email):
#     client.clario_stepimpl.enter_email(client, email)
#     time.sleep(5)


@when("User enters Email from JSON")
def enter_email(client):
    client.clario_stepimpl.enter_email(client)


@when("User enters Confirm Email from JSON")
def enter_confirm_email(client):
    client.clario_stepimpl.enter_confirm_email(client)


@when("User enters First Name from JSON")
def enter_first_name(client):
    client.clario_stepimpl.enter_first_name(client)


@when("User enters Last Name from JSON")
def enter_last_name(client):
    client.clario_stepimpl.enter_last_name(client)


@when("User enters Password from JSON")
def enter_password(client):
    client.clario_stepimpl.enter_password(client)


@when("User enters Confirm Password from JSON")
def enter_confirm_password(client):
    client.clario_stepimpl.enter_confirm_password(client)


@then("User details should be entered successfully")
def verify_user_details():
    print("User details entered successfully.")






