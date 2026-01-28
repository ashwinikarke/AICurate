
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_lifecycle_state_display():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://example.com/dashboard")
        driver.find_element(By.ID, "workflows").click()
        assert "Draft" in driver.page_source
        assert "Review" in driver.page_source
        assert "Published" in driver.page_source
        print("Lifecycle states displayed correctly in workflow tabs")
    finally:
        driver.quit()
