
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_access_protected_workflow_without_login():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://example.com/protected_workflow")
        time.sleep(2)
        assert "Login" in driver.title
        print("Redirected to login when accessing protected workflow")
    finally:
        driver.quit()
