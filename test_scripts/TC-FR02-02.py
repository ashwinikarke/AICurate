
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def filter_data_invalid(url):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "dataPage"))
        )
        driver.find_element(By.ID, "startDatePicker").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//td[contains(@data-date, '2023-01-01')]").click()
        driver.find_element(By.ID, "endDatePicker").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//td[contains(@data-date, '2023-01-01')]").click()
        driver.find_element(By.ID, "applyFilterButton").click()
        error_message = driver.find_element(By.ID, "errorElement").text
        assert error_message == "End date must be after start date"
        print("Error message displayed for invalid date range.")
    except Exception as e:
        print(f"Failed to filter data: {e}")
    finally:
        driver.quit()
filter_data_invalid('http://example.com/data')
