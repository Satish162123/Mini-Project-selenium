import pytest
import json
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def read_login_json():
    with open("test_data/login_data.json") as file:
        return json.load(file)
    
@pytest.mark.regression
@pytest.mark.parametrize(
    "data",
    read_login_json()
)
def test_login_with_json(driver, data):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.load()
    login_page.login(data["username"], data["password"])

    if data["expected"] == "success":
        assert inventory_page.is_loaded()
    else:
        assert "Username and password do not match" in login_page.get_error_message()