
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def clear_filters(url):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "dataPage"))
        )
        driver.find_element(By.ID, "clearFiltersButton").click()
        time.sleep(1)
        data_displayed = driver.find_element(By.ID, "dataContainer").is_displayed()
        assert data_displayed == True
        print("Filters cleared successfully, data is displayed.")
    except Exception as e:
        print(f"Failed to clear filters: {e}")
    finally:
        driver.quit()
clear_filters('http://example.com/data')
