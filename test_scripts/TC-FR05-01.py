
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_access_protected_workflow():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://example.com/dashboard")
        driver.find_element(By.ID, "workflows").click()
        driver.find_element(By.XPATH, "//a[contains(text(), 'Protected Workflow')]").click()
        assert "Protected Workflow" in driver.title
        print("Accessed protected workflow without issues")
    finally:
        driver.quit()
