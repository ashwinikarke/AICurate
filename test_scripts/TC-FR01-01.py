
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_login_page_accessible():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://example.com/login")
        assert "Login" in driver.title, "Login page not loaded."
        assert driver.find_element(By.ID, "username").is_displayed()
        assert driver.find_element(By.ID, "password").is_displayed()
    finally:
        driver.quit()
