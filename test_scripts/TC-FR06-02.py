
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_empty_workflow_categories_display():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://example.com/dashboard")
        driver.find_element(By.ID, "workflows").click()
        assert "No workflows available" in driver.page_source
        print("Correctly displayed message for no available workflows")
    finally:
        driver.quit()
