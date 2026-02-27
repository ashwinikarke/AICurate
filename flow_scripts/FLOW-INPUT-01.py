from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# CONFIGURATION 
BASE_URL = "https://app-under-test/input-data-management"
VALID_JSON_FILE_PATH = "/path/to/valid.json"
VALID_CSV_FILE_PATH = "/path/to/valid.csv"
INVALID_FILE_PATH = "/path/to/invalid.txt"

# Locators (adjust per application)
UPLOAD_SECTION = (By.ID, "uploadSection")
UPLOAD_JSON_BUTTON = (By.ID, "uploadJsonBtn")
UPLOAD_CSV_BUTTON = (By.ID, "uploadCsvBtn")
INVALID_FILE_MESSAGE = (By.CLASS_NAME, "toast-error")
CLEAR_ALL_BUTTON = (By.ID, "clearAllBtn")
INPUT_FIELD_1 = (By.ID, "inputField1")
INPUT_FIELD_2 = (By.ID, "inputField2")
CONFIRMATION_MESSAGE = (By.CLASS_NAME, "toast-success")

# ----------------------------
# TEST FLOW (EXECUTION SCRIPT)
# Covers: FR-07 → FR-19
# ----------------------------
def test_input_data_management_flow():
    # WebDriver setup using WebDriverManager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    wait = WebDriverWait(driver, 10)

    try:
        # Step 1: Open Input Data Management Page (FR-07)
        driver.get(BASE_URL)
        wait.until(EC.visibility_of_element_located(UPLOAD_SECTION))

        # Step 2: Upload a valid JSON file (FR-07)
        driver.find_element(*UPLOAD_JSON_BUTTON).send_keys(VALID_JSON_FILE_PATH)
        time.sleep(2)  # Wait for the upload process, adjust as necessary

        # Step 3: Validate successful upload message
        assert "success" in driver.page_source, "Valid JSON file upload should be successful"

        # Step 4: Upload a valid CSV file (FR-10)
        driver.find_element(*UPLOAD_CSV_BUTTON).send_keys(VALID_CSV_FILE_PATH)
        time.sleep(2)  # Wait for the upload process

        # Step 5: Validate successful upload message
        assert "success" in driver.page_source, "Valid CSV file upload should be successful"

        # Step 6: Attempt to upload an invalid file type (FR-11)
        driver.find_element(*UPLOAD_JSON_BUTTON).send_keys(INVALID_FILE_PATH)
        time.sleep(2)  # Wait for the error message

        # Step 7: Validate error message for unsupported file type
        error_message = wait.until(EC.visibility_of_element_located(INVALID_FILE_MESSAGE))
        assert "unsupported" in error_message.text.lower(), "Error message should indicate unsupported file type"

        # Step 8: Trigger correct error message display (FR-12)
        driver.find_element(*UPLOAD_JSON_BUTTON).send_keys(INVALID_FILE_PATH)
        time.sleep(2)  # Wait for the error message
        error_message = wait.until(EC.visibility_of_element_located(INVALID_FILE_MESSAGE))
        assert error_message.is_displayed(), "Red toast error message should be displayed"

        # Step 9: Fill multiple input fields for testing clear functionality (FR-19)
        driver.find_element(*INPUT_FIELD_1).send_keys("Sample Data 1")
        driver.find_element(*INPUT_FIELD_2).send_keys("Sample Data 2")

        # Step 10: Click the Clear All button (FR-19)
        driver.find_element(*CLEAR_ALL_BUTTON).click()
        time.sleep(1)  # Small wait for visual confirmation

        # Step 11: Validate confirmation message for clearing fields
        confirmation_message = wait.until(EC.visibility_of_element_located(CONFIRMATION_MESSAGE))
        assert confirmation_message.is_displayed(), "Confirmation message for clearing fields should be shown"

    finally:
        driver.quit()