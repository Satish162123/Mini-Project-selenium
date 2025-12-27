import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from datetime import datetime

driver_path = "F:/Satish/chromedriver-win64/chromedriver.exe"

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(driver_path))
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            screenshots_dir = os.path.join(os.path.dirname(__file__), "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)

            file_name = f"{item.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            file_path = os.path.join(screenshots_dir, file_name)

            driver.save_screenshot(file_path)
        
        '''if driver: 
            os.makedirs("screenshots", exist_ok=True) 
            driver.save_screenshot( 
                f"screenshots/{item.name}_{datetime.now().strftime('%H%M%S')}.png" 
            )''' 