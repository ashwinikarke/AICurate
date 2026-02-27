from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# CONFIGURATION 
BASE_URL = "https://app-under-test/constants"
VALID_JSON = '{"key1": "value1", "key2": "value2"}'
DELETION_CONFIRMATION_TEXT = "Are you sure you want to delete this constant?"
CLEAR_ALL_CONFIRMATION_TEXT = "Are you sure you want to clear all constants?"

# Locators (adjust per application)
CONSTANTS_FIELD = (By.ID, "constantsField")
ADD_CONSTANT_BUTTON = (By.ID, "addConstantBtn")
DELETE_CONSTANT_BUTTON = (By.ID, "deleteConstantBtn")
CLEAR_ALL_BUTTON = (By.ID, "clearAllBtn")
CONFIRM_DELETE = (By.CLASS_NAME, "confirm-delete")
CONFIRM_CLEAR_ALL = (By.CLASS_NAME, "confirm-clear-all")
CONSTANTS_LIST = (By.ID, "constantsList")
ERROR_MESSAGE = (By.CLASS_NAME, "error-message")

# ----------------------------
# TEST FLOW (EXECUTION SCRIPT)
# Covers: FR-24 → FR-27
# ----------------------------
def test_constants_management_flow():
    # WebDriver setup using WebDriverManager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    wait = WebDriverWait(driver, 10)

    try:
        # Step 1: Open Constants Management Page (FR-24)
        driver.get(BASE_URL)

        # Step 2: Verify constants field is loaded (FR-24)
        constants_field = wait.until(EC.visibility_of_element_located(CONSTANTS_FIELD))
        assert constants_field.is_displayed(), "Constants field should be displayed"

        # Step 3: Enter valid single-level JSON structure (FR-24)
        constants_field.clear()
        constants_field.send_keys(VALID_JSON)
        driver.find_element(*ADD_CONSTANT_BUTTON).click()

        # Step 4: Verify constant is accepted and displayed (FR-24)
        constants_list = wait.until(EC.visibility_of_element_located(CONSTANTS_LIST))
        assert VALID_JSON in constants_list.text, "The constant should be displayed in the list"

        # Step 5: Select a constant and initiate deletion (FR-25)
        delete_button = driver.find_element(*DELETE_CONSTANT_BUTTON)
        delete_button.click()

        # Step 6: Confirm deletion (FR-25)
        confirm_button = wait.until(EC.visibility_of_element_located(CONFIRM_DELETE))
        assert confirm_button.text == DELETION_CONFIRMATION_TEXT, "Deletion confirmation dialog should appear"
        confirm_button.click()

        # Step 7: Verify constant is removed (FR-25)
        assert VALID_JSON not in constants_list.text, "The constant should be removed from the list"

        # Step 8: Click 'Clear All' button (FR-27)
        driver.find_element(*CLEAR_ALL_BUTTON).click()

        # Step 9: Confirm clearing all constants (FR-27)
        confirm_clear_button = wait.until(EC.visibility_of_element_located(CONFIRM_CLEAR_ALL))
        assert confirm_clear_button.text == CLEAR_ALL_CONFIRMATION_TEXT, "Clear all confirmation dialog should appear"
        confirm_clear_button.click()

        # Step 10: Verify all constants are cleared (FR-27)
        assert constants_list.text == "", "All constants should be cleared from the list"

    finally:
        driver.quit()