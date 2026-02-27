from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# CONFIGURATION 
BASE_URL = "https://app-under-test/workflow"
VALID_WORKFLOW_NAME = "Test Workflow"
INVALID_WORKFLOW_NAME = ""
WORKFLOW_DESCRIPTION = "This is a test workflow."

# Locators (adjust per application)
CREATE_WORKFLOW_BUTTON = (By.ID, "createWorkflowBtn")
WORKFLOW_NAME_INPUT = (By.ID, "workflowName")
WORKFLOW_DESC_INPUT = (By.ID, "workflowDescription")
SUBMIT_BUTTON = (By.ID, "submitBtn")
ERROR_MESSAGE = (By.CLASS_NAME, "error-message")
CONFIRMATION_MESSAGE = (By.ID, "confirmationMsg")
WORKFLOW_CARD = (By.CLASS_NAME, "workflow-card")
CONFIGURATION_PAGE_INDICATOR = (By.ID, "configurationPage")

# ----------------------------
# TEST FLOW (EXECUTION SCRIPT)
# Covers: FR-01 → FR-05, FR-09, FR-22
# ----------------------------
def test_create_and_configure_workflow():
    # WebDriver setup using WebDriverManager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    wait = WebDriverWait(driver, 10)

    try:
        # Step 1: Navigate to the workflow creation page (FR-01)
        driver.get(BASE_URL)
        driver.find_element(*CREATE_WORKFLOW_BUTTON).click()

        # Step 2: Fill in valid information (FR-01)
        wait.until(EC.visibility_of_element_located(WORKFLOW_NAME_INPUT)).send_keys(VALID_WORKFLOW_NAME)
        wait.until(EC.visibility_of_element_located(WORKFLOW_DESC_INPUT)).send_keys(WORKFLOW_DESCRIPTION)

        # Step 3: Click 'Create' (FR-01)
        driver.find_element(*SUBMIT_BUTTON).click()
        confirmation = wait.until(EC.visibility_of_element_located(CONFIRMATION_MESSAGE))
        assert "successfully" in confirmation.text.lower(), "Workflow should be created successfully."

        # Step 4: Attempt to create a workflow rule with missing mandatory fields (FR-01)
        driver.get(BASE_URL)
        driver.find_element(*CREATE_WORKFLOW_BUTTON).click()
        wait.until(EC.visibility_of_element_located(SUBMIT_BUTTON)).click()

        error = wait.until(EC.visibility_of_element_located(ERROR_MESSAGE))
        assert "mandatory" in error.text.lower(), "Error message should appear for mandatory fields."

        # Step 5: Navigate to workflow listing and click on a workflow card (FR-05)
        driver.get(BASE_URL)
        workflow_card = wait.until(EC.visibility_of_element_located(WORKFLOW_CARD))
        workflow_card.click()

        # Step 6: Verify navigation to the correct workflow configuration page (FR-05)
        wait.until(EC.visibility_of_element_located(CONFIGURATION_PAGE_INDICATOR))

        # Step 7: Attempt to submit form with empty name field (FR-09)
        driver.get(BASE_URL)
        driver.find_element(*CREATE_WORKFLOW_BUTTON).click()
        wait.until(EC.visibility_of_element_located(WORKFLOW_DESC_INPUT)).send_keys(WORKFLOW_DESCRIPTION)
        driver.find_element(*SUBMIT_BUTTON).click()
        
        error = wait.until(EC.visibility_of_element_located(ERROR_MESSAGE))
        assert "mandatory" in error.text.lower(), "Error message should appear for empty name field."

        # Step 8: Submit valid configurations and confirm saving (FR-22)
        driver.find_element(*WORKFLOW_NAME_INPUT).send_keys(VALID_WORKFLOW_NAME)
        driver.find_element(*SUBMIT_BUTTON).click()
        confirmation = wait.until(EC.visibility_of_element_located(CONFIRMATION_MESSAGE))
        assert "successfully" in confirmation.text.lower(), "Configuration should be saved successfully."

    finally:
        driver.quit()