from unittest.mock import MagicMock
from pages.super_demo import DemoPage

def test_super_click():
    page = DemoPage(MagicMock())  # Create DemoPage with a mock driver

    page.click(("id", "sample"))  # Call the child method

    print("Test completed")