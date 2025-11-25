
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def filter_data(url, start_date, end_date):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "dataPage"))
        )
        driver.find_element(By.ID, "startDatePicker").click()
        time.sleep(1)
        driver.find_element(By.XPATH, f"//td[contains(@data-date, '{start_date}')]").click()
        driver.find_element(By.ID, "endDatePicker").click()
        time.sleep(1)
        driver.find_element(By.XPATH, f"//td[contains(@data-date, '{end_date}')]").click()
        driver.find_element(By.ID, "applyFilterButton").click()
        print("Filter applied successfully.")
    except Exception as e:
        print(f"Failed to filter data: {e}")
    finally:
        driver.quit()
filter_data('http://example.com/data', '2023-01-01', '2023-01-31')
