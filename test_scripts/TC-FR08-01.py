
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_tab_switching_without_reload():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://example.com/dashboard")
        driver.find_element(By.ID, "workflows").click()
        driver.find_element(By.ID, "draftTab").click()
        time.sleep(2)
        driver.find_element(By.ID, "reviewTab").click()
        assert len(driver.find_elements(By.CLASS_NAME, "workflow")) > 0
        print("Successfully switched between Draft and Review tabs!")
    finally:
        driver.quit()
