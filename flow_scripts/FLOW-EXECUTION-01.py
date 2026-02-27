from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# CONFIGURATION 
BASE_URL = "https://app-under-test/workflows"
WORKFLOW_NAME = "Sample Workflow"

# Locators (adjust per application)
WORKFLOW_LISTING = (By.ID, "workflowListing")  
EXECUTE_BUTTON = (By.XPATH, "//button[contains(text(), 'Execute')]")
CONFIRMATION_MESSAGE = (By.CLASS_NAME, "confirmation-message")
SIMULATION_PAGE_HEADER = (By.ID, "simulationPageHeader")
INDIVIDUAL_TESTING_OPTIONS = (By.CLASS_NAME, "individual-testing-options")
INPUT_FIELD = (By.ID, "inputField")
SUBMIT_BUTTON = (By.ID, "submitBtn")
RESULTS_PAGE = (By.ID, "resultsPage")
RESULT_STATUS = (By.CLASS_NAME, "result-status")
INPUT_DATA_DISPLAY = (By.CLASS_NAME, "input-data")
TIMING_INFO = (By.CLASS_NAME, "timing-info")

# ----------------------------
# TEST FLOW (EXECUTION SCRIPT)
# Covers: FR-37 → FR-40
# ----------------------------
def test_workflow_execution():
    # WebDriver setup using WebDriverManager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    wait = WebDriverWait(driver, 10)

    try:
        # Step 1: Navigate to workflows listing page (FR-37)
        driver.get(BASE_URL)
        assert wait.until(EC.visibility_of_element_located(WORKFLOW_LISTING)).is_displayed(), "Workflows listing should be displayed"

        # Step 2: Select a workflow and click 'Execute' (FR-37)
        execute_button = wait.until(EC.element_to_be_clickable(EXECUTE_BUTTON))
        execute_button.click()
        assert wait.until(EC.visibility_of_element_located(CONFIRMATION_MESSAGE)).is_displayed(), "Confirmation message should be displayed after execution initiation"

        # Step 3: Navigate to simulation page (FR-38)
        driver.get(BASE_URL + "/simulation")
        assert wait.until(EC.visibility_of_element_located(SIMULATION_PAGE_HEADER)).is_displayed(), "Simulation page should load successfully"
        
        # Step 4: Confirm presence of options for individual testing (FR-38)
        assert wait.until(EC.visibility_of_element_located(INDIVIDUAL_TESTING_OPTIONS)).is_displayed(), "Individual testing options should be visible"

        # Step 5: Start a workflow execution with valid inputs (FR-39)
        input_field = wait.until(EC.visibility_of_element_located(INPUT_FIELD))
        input_field.send_keys("Valid Input")
        wait.until(EC.element_to_be_clickable(SUBMIT_BUTTON)).click()
        assert wait.until(EC.visibility_of_element_located(RESULTS_PAGE)).is_displayed(), "Results page should be displayed after submission"

        # Step 6: Check for execution status and details (FR-40)
        result_status = wait.until(EC.visibility_of_element_located(RESULT_STATUS))
        input_data = driver.find_element(*INPUT_DATA_DISPLAY)
        timing_info = driver.find_element(*TIMING_INFO)
        
        assert result_status.is_displayed(), "Execution status should be displayed"
        assert input_data.is_displayed(), "Input data should be displayed"
        assert timing_info.is_displayed(), "Timing information should be displayed"

    finally:
        driver.quit()