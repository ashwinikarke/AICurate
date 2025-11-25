
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def test_invalid_filter_date():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        # Step 1: Navigate to data page
        driver.get("http://example.com/data")
        # Step 2: Select Start Date
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "startDate"))).click()
        # Step 3: Pick a valid start date
        driver.find_element(By.XPATH, "//td[@data-day='10']").click()
        # Step 4: Select End Date
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "endDate"))).click()
        # Step 5: Pick an earlier end date than start date
        driver.find_element(By.XPATH, "//td[@data-day='5']").click()
        # Step 6: Click 'Apply Filters'
        driver.find_element(By.ID, "applyFilters").click()
        # Assertion for error message
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Invalid date range')]"))) 
        assert "Invalid date range" in driver.page_source
        print("Error message displayed for invalid date range.")
    except Exception as e:
        print(f"Failed: {e}")
    finally:
        driver.quit()
test_invalid_filter_date()