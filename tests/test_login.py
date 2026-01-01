import pytest 
from pages.login_page import LoginPage 
from pages.inventory_page import InventoryPage 
from utils.config_reader import ConfigReader 
 
 
@pytest.mark.smoke 
def test_login_with_valid_credentials(driver): 
    """ 
    TC01: Verify user can login with valid credentials 
    """ 
    login = LoginPage(driver) 
    inventory = InventoryPage(driver) 
 
    login.load() 
    login.login( 
        ConfigReader.get("credentials", "valid_username"), 
        ConfigReader.get("credentials", "valid_password") 
    ) 
 
    assert inventory.is_loaded() 
 
 
@pytest.mark.regression 
def test_login_with_invalid_credentials(driver): 
    """ 
    TC02: Verify error message for invalid login 
    """ 
    login = LoginPage(driver) 
 
    login.load() 
    login.login( 
        ConfigReader.get("credentials", "invalid_username"), 
        ConfigReader.get("credentials", "invalid_password") 
    ) 
 
    assert "Username and password do not match" in login.get_error_message()


 
@pytest.mark.regression 
def test_login_with_empty_username(driver): 
    """ 
    TC03: Verify error when username is empty 
    """ 
    login = LoginPage(driver) 
 
    login.load() 
    login.login("", "some_password") 
 
    assert "Username is required" in login.get_error_message() 
 
 
@pytest.mark.regression 
def test_login_with_empty_password(driver): 
    """ 
    TC04: Verify error when password is empty 
    """ 
    login = LoginPage(driver) 
 
    login.load() 
    login.login("standard_user", "") 
 
    assert "Password is required" in login.get_error_message()


def test_login_with_locked_user(driver): 
    """ 
    TC05: Verify locked user cannot login 
    """ 
    login = LoginPage(driver) 
 
    login.load() 
    login.login("locked_out_user", "secret_sauce") 
 
    assert "locked out" in login.get_error_message().lower()

@pytest.mark.regression 
def test_login_with_username_spaces(driver): 
    """ 
    TC06: Verify login trims username spaces 
    """ 
    login = LoginPage(driver) 
    inventory = InventoryPage(driver) 
 
    login.load() 
    login.login(" standard_user ", "secret_sauce") 
 
    assert inventory.is_loaded() 

@pytest.mark.regression 
def test_login_sql_injection_attempt(driver): 
    """ 
    TC07: Verify SQL injection is handled safely 
    """ 
    login = LoginPage(driver) 
 
    login.load() 
    login.login("' OR '1'='1", "any_password") 
 
    assert "error" in login.get_error_message().lower() 