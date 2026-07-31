import pytest
import time
from pages.clario_pages.clario_page import ClarioPage

@pytest.mark.parametrize(
    "email",
    [
        "pavan@gmail.com",
        "rahul@gmail.com",
        "john@gmail.com"
    ]
)

def test_clario_email(client, email):
    client.clario_stepimpl.launch_application(client)
    time.sleep(5)
    client.clario_stepimpl.click_on_create_account(client)
    page = ClarioPage(client.driver)
    page.enter_email(email)