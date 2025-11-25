
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def test_filter_pro_number():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        # Step 1: Navigate to dataset page
        driver.get("http://example.com/dataset")
        # Step 2: Click filter menu
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "filterButton"))).click()
        # Step 3: Select filter criterion 'Contains'
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//option[contains(text(), 'Contains')]"))).click()
        # Step 4: Enter a valid PRO Number
        driver.find_element(By.ID, "proNumberInput").send_keys("PRO12345")
        # Step 5: Click 'Apply'
        driver.find_element(By.ID, "applyFilters").click()
        # Assertion for filtered results
        assert "Filtered results" in driver.page_source
        print("Filtered results displayed correctly based on PRO Number.")
    except Exception as e:
        print(f"Failed: {e}")
    finally:
        driver.quit()
test_filter_pro_number()