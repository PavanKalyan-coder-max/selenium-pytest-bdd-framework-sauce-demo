from pytest_bdd import scenarios, given, when, then
import time
from pytest_bdd import parsers

scenarios("../features/login.feature")
scenarios("../features/logout.feature")
# scenarios("../features/Communication.feature")
# scenarios("../features/products.feature")


@given("User launches SauceDemo application")
def launch_application(client):
    client.login_stepimpl.launch_application(client)


# @when("User enters valid username and password")
# def login(client):
#     time.sleep(5)
#     client.login_stepimpl.login_to_application(client)

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






