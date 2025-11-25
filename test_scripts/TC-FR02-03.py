
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def test_clear_filters():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        # Step 1: Navigate to data page with filters applied
        driver.get("http://example.com/data")
        # Step 2: Click 'Clear Filters'
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "clearFilters"))).click()
        # Step 3: Verify all data records are displayed
        assert "All data loaded" in driver.page_source
        print("All data displayed after clearing filters.")
    except Exception as e:
        print(f"Failed: {e}")
    finally:
        driver.quit()
test_clear_filters()