import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.config_reader import ConfigReader


@pytest.mark.regression
@pytest.mark.parametrize(
    "username,password,expected_result",
    [
        (
            ConfigReader.get("credentials", "valid_username"),
            ConfigReader.get("credentials", "valid_password"),
            True
        ),
        (
            ConfigReader.get("credentials", "invalid_username"),
            ConfigReader.get("credentials", "invalid_password"),
            False
        )
    ]
)
def test_login_parametrized(driver, username, password, expected_result):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.load()
    login_page.login(username, password)

    if expected_result:
        assert inventory_page.is_loaded()
    else:
        assert "Username and password do not match" in login_page.get_error_message()
