import pytest
import csv
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def read_login_csv():
    data = []
    with open("test_data/login_data.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(
                (row["username"], row["password"], row["result"])
            )
    return data

@pytest.mark.regression
@pytest.mark.parametrize(
    "username,password,result",
    read_login_csv()
)
def test_login_with_csv(driver, username, password, result):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.load()
    login_page.login(username, password)

    if result == "success":
        assert inventory_page.is_loaded()
    else:
        assert "Username and password do not match" in login_page.get_error_message()