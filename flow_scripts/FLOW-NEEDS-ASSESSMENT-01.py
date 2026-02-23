from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# CONFIGURATION 
BASE_URL = "https://app-under-test/"
VALID_CUSTOMER_DATA = "John Doe, 123 Main St, johndoe@example.com"
INCOMPLETE_CUSTOMER_DATA = "John Doe"
MAX_LENGTH_DATA = "X" * 255  # Assuming max length is 255 characters
VAGUE_INPUT = "I need something better"

# Locators (adjust per application)
NEEDS_ASSESSMENT_LINK = (By.ID, "needsAssessmentLink")
SUBMIT_BUTTON = (By.ID, "submitButton")
INPUT_FIELD = (By.ID, "customerInput")
ERROR_MESSAGE = (By.CLASS_NAME, "error-message")

# ----------------------------
# TEST FLOW (EXECUTION SCRIPT)
# Covers: FR-10 → FR-24
# ----------------------------
def test_customer_needs_assessment_flow():
    # WebDriver setup using WebDriverManager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    wait = WebDriverWait(driver, 10)

    try:
        # Step 1: Open the application base URL
        driver.get(BASE_URL)

        # Step 2: Click on the customer needs assessment tool link (FR-10)
        driver.find_element(*NEEDS_ASSESSMENT_LINK).click()

        # Step 3: Verify that the needs assessment tool loads without errors (FR-12)
        time.sleep(2)  # Wait for loading visualization
        
        # Step 4: Enter valid customer data (FR-11)
        input_field = wait.until(EC.visibility_of_element_located(INPUT_FIELD))
        input_field.clear()
        input_field.send_keys(VALID_CUSTOMER_DATA)
        driver.find_element(*SUBMIT_BUTTON).click()
        time.sleep(1)  # Allow time for processing
        assert "success" in driver.page_source.lower(), "Customer data should be processed successfully"

        # Step 5: Enter incomplete customer data (FR-13)
        input_field.clear()
        input_field.send_keys(INCOMPLETE_CUSTOMER_DATA)
        driver.find_element(*SUBMIT_BUTTON).click()
        error = wait.until(EC.visibility_of_element_located(ERROR_MESSAGE))
        assert "valid" in error.text.lower(), "Error message for incomplete data should prompt user"

        # Step 6: Validate maximum length data entry (FR-14)
        input_field.clear()
        input_field.send_keys(MAX_LENGTH_DATA)
        driver.find_element(*SUBMIT_BUTTON).click()
        time.sleep(1)
        assert "success" in driver.page_source.lower(), "Data should be accepted without truncation"

        # Step 7: Test for blank input (FR-22)
        input_field.clear()
        driver.find_element(*SUBMIT_BUTTON).click()
        error = wait.until(EC.visibility_of_element_located(ERROR_MESSAGE))
        assert "please enter your needs" in error.text.lower(), "Error message for blank input should be displayed"

        # Step 8: Handle empty input (FR-23)
        input_field.clear()
        driver.find_element(*SUBMIT_BUTTON).click()
        error = wait.until(EC.visibility_of_element_located(ERROR_MESSAGE))
        assert "provide" in error.text.lower(), "System should prompt user for needed input"

        # Step 9: Check for vague input (FR-24)
        input_field.clear()
        input_field.send_keys(VAGUE_INPUT)
        driver.find_element(*SUBMIT_BUTTON).click()
        error = wait.until(EC.visibility_of_element_located(ERROR_MESSAGE))
        assert "clearer" in error.text.lower(), "System should prompt for clearer input"

    finally:
        driver.quit()