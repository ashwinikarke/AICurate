
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

def test_switch_tabs_with_no_connection():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://example.com/dashboard")
        driver.find_element(By.ID, "workflows").click()
        os.system("ipconfig /release")
        driver.find_element(By.ID, "draftTab").click()
        time.sleep(2)
        assert "No Internet Connection" in driver.page_source
        print("User informed of connectivity issue while switching tabs")
    finally:
        driver.quit()
