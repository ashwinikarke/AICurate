
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_successful_login():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://example.com/login")
        driver.find_element(By.ID, "username").send_keys("validUser")
        driver.find_element(By.ID, "password").send_keys("validPassword")
        driver.find_element(By.ID, "loginButton").click()
        assert "Dashboard" in driver.title, "User not redirected to dashboard."
    finally:
        driver.quit()
