
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_invalid_login():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://example.com/login")
        driver.find_element(By.ID, "username").send_keys("invalid_user")
        driver.find_element(By.ID, "password").send_keys("invalid_pass")
        driver.find_element(By.ID, "loginBtn").click()
        error_message = driver.find_element(By.ID, "error").text
        assert error_message == "Invalid credentials"
        print("Error message displayed for invalid credentials")
    finally:
        driver.quit()
