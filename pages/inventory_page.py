from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    INVENTORY = (By.CLASS_NAME, "inventory_list")

    def is_loaded(self):
        return self.is_visible(self.INVENTORY)
    