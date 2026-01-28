
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_display_workflow_categories():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://example.com/dashboard")
        driver.find_element(By.ID, "workflows").click()
        assert driver.find_element(By.ID, "draftTab").is_displayed() 
        assert driver.find_element(By.ID, "reviewTab").is_displayed() 
        assert driver.find_element(By.ID, "publishedTab").is_displayed() 
        print("All categorized workflow tabs displayed successfully")
    finally:
        driver.quit()
