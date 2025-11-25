
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def filter_pro_number_invalid(url, invalid_pro_number):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "dataPage"))
        )
        driver.find_element(By.ID, "filterMenu").click()
        time.sleep(1)
        driver.find_element(By.ID, "filterOptionContains").click()
        driver.find_element(By.ID, "proNumberInput").send_keys(invalid_pro_number)
        driver.find_element(By.ID, "applyFilterButton").click()
        error_message = driver.find_element(By.ID, "errorElement").text
        assert error_message == "No results found"
        print("Error message displayed for invalid PRO Number.")
    except Exception as e:
        print(f"Failed to filter by invalid PRO Number: {e}")
    finally:
        driver.quit()
filter_pro_number_invalid('http://example.com/data', 'INVALID123')
