
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_blank_login():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://example.com/login")
        driver.find_element(By.ID, "loginBtn").click()
        assert driver.find_element(By.ID, "username").text == ""
        assert driver.find_element(By.ID, "password").text == ""
        print("Login button is disabled for empty fields")
    finally:
        driver.quit()
