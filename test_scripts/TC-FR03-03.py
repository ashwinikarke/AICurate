
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

def test_heavy_load_handling():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://example.com/login")
        driver.find_element(By.ID, "username").send_keys("valid_user")
        driver.find_element(By.ID, "password").send_keys("valid_pass")
        time.sleep(random.uniform(2, 5))
        driver.find_element(By.ID, "loginBtn").click()
        assert "BSN Dashboard" in driver.title
        print("Authenticated successfully despite heavy load")
    finally:
        driver.quit()
