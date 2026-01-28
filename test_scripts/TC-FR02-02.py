
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_failed_redirect():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://example.com/login")
        driver.find_element(By.ID, "username").send_keys("valid_user")
        driver.find_element(By.ID, "password").send_keys("valid_pass")
        driver.find_element(By.ID, "loginBtn").click()
        time.sleep(2)
        assert "Error" in driver.page_source
        print("Failed to redirect and user received an error message")
    finally:
        driver.quit()
