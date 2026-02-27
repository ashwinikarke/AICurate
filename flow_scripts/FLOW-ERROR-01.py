from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# CONFIGURATION
BASE_URL = "https://app-under-test/error-handling"
VALID_JSON_FILE_PATH = "/path/to/valid.json"
LARGE_FILE_PATH = "/path/to/large_file_4MB.zip"  # Example of a file under 5MB
INVALID_DATA = "Invalid Data"

# Locators (adjust per application)
UPLOAD_SECTION = (By.ID, "uploadSection")
UPLOAD_BUTTON = (By.ID, "uploadBtn")
ERROR_MESSAGE = (By.CLASS_NAME, "error-message")
INPUT_FIELD = (By.ID, "inputField")
SUBMIT_BUTTON = (By.ID, "submitBtn")
SUCCESS_MESSAGE = (By.CLASS_NAME, "success-message")

# ----------------------------
# TEST FLOW (EXECUTION SCRIPT)
# Covers: FR-03, NFR-01, NFR-02, NFR-08
# ----------------------------
def test_error_handling_and_validation_flow():
    # WebDriver setup using WebDriverManager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    wait = WebDriverWait(driver, 10)

    try:
        # Step 1: Open Error Handling Page (FR-03)
        driver.get(BASE_URL)

        # Step 2: Navigate to upload section (NFR-01, NFR-02)
        wait.until(EC.visibility_of_element_located(UPLOAD_SECTION))

        # Step 3: Upload a valid JSON file (NFR-02)
        upload_btn = driver.find_element(*UPLOAD_BUTTON)
        upload_btn.send_keys(VALID_JSON_FILE_PATH)
        wait.until(EC.visibility_of_element_located(SUCCESS_MESSAGE))
        
        # Step 4: Trigger inline validation error (NFR-08)
        input_field = driver.find_element(*INPUT_FIELD)
        input_field.send_keys(INVALID_DATA)  # Enter invalid data
        submit_btn = driver.find_element(*SUBMIT_BUTTON)
        submit_btn.click()

        # Step 5: Confirm inline validation message appears (NFR-08)
        error_message = wait.until(EC.visibility_of_element_located(ERROR_MESSAGE))
        assert "specific error" in error_message.text.lower(), "Inline validation message did not appear as expected"

        # Step 6: Upload file within size limit (NFR-01)
        upload_btn.send_keys(LARGE_FILE_PATH)
        wait.until(EC.visibility_of_element_located(SUCCESS_MESSAGE))

        # Step 7: Trigger an exception condition (FR-03)
        input_field.clear()  # Clear input field to trigger error
        input_field.send_keys("")  # Intentionally leave blank
        submit_btn.click()
        
        # Step 8: Observe and assert error response is displayed (FR-03)
        error_message = wait.until(EC.visibility_of_element_located(ERROR_MESSAGE))
        assert "error" in error_message.text.lower(), "Custom error message for exception was not displayed"

    finally:
        driver.quit()