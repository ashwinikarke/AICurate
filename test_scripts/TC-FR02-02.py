
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_login_with_incorrect_password():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://example.com/login")
        driver.find_element(By.ID, "username").send_keys("validUser")
        driver.find_element(By.ID, "password").send_keys("incorrectPassword")
        driver.find_element(By.ID, "loginButton").click()
        assert driver.find_element(By.ID, "errorMessage").is_displayed(), "Error message not displayed for incorrect password.";
    finally:
        driver.quit()
