
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_session_expiration_access():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://example.com/login")
        driver.find_element(By.ID, "username").send_keys("valid_user")
        driver.find_element(By.ID, "password").send_keys("valid_pass")
        driver.find_element(By.ID, "loginBtn").click()
        time.sleep(65)  # Simulate session expiration
        driver.get("http://example.com/protected_workflow")
        assert "Login" in driver.title
        print("Redirected to login after session expiration")
    finally:
        driver.quit()
