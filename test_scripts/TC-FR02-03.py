
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

def test_network_failure():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://example.com/login")
        driver.find_element(By.ID, "username").send_keys("valid_user")
        driver.find_element(By.ID, "password").send_keys("valid_pass")
        driver.find_element(By.ID, "loginBtn").click()
        os.system("ipconfig /release")
        time.sleep(1)
        assert "Network Error" in driver.page_source
        print("Network error displayed due to simulated failure")
    finally:
        driver.quit()
