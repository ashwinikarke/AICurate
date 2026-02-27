from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

# CONFIGURATION 
BASE_URL = "https://app-under-test/configuration"
VALID_NESTED_JSON = '{"person":{"name":"John","age":30,"address":{"street":"123 Main St","city":"New York"}}}'
ENUM_ATTRIBUTE = "exampleEnum"
VIEW_DETAILS_BUTTON_TEXT = "View Details"
DETAILED_JSON_MODAL = (By.ID, "jsonDataModal")

# Locators (adjust per application)
INPUT_FIELD = (By.ID, "jsonInputField")
SETTINGS_BUTTON = (By.ID, "settingsButton")
ENUM_INPUT_FIELD = (By.ID, "enumInputField")
SAVE_BUTTON = (By.ID, "saveButton")
DETAILED_JSON_DISPLAY = (By.ID, "detailedJsonDisplay")

# ----------------------------
# TEST FLOW (EXECUTION SCRIPT)
# Covers: FR-15 → FR-18
# ----------------------------
def test_input_parameter_configuration_flow():
    # WebDriver setup using WebDriverManager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    wait = WebDriverWait(driver, 10)

    try:
        # Step 1: Open Input Configuration Page (FR-15)
        driver.get(BASE_URL)

        # Step 2: Verify input field loaded successfully (FR-15)
        input_field = wait.until(EC.visibility_of_element_located(INPUT_FIELD))
        assert input_field.is_displayed(), "Input field for JSON should be displayed"

        # Step 3: Enter valid nested JSON structure (FR-15)
        input_field.clear()
        input_field.send_keys(VALID_NESTED_JSON)
        # Add a small delay to ensure input is accepted visually
        input_field_value = input_field.get_attribute('value')
        assert json.loads(input_field_value) == json.loads(VALID_NESTED_JSON), "Nested JSON structure should be accepted"

        # Step 4: Open input field settings to configure ENUM attribute (FR-17)
        driver.find_element(*SETTINGS_BUTTON).click()
        enum_input_field = wait.until(EC.visibility_of_element_located(ENUM_INPUT_FIELD))
        assert enum_input_field.is_displayed(), "ENUM attribute input field should be displayed"

        # Step 5: Configure ENUM attribute (FR-17)
        enum_input_field.clear()
        enum_input_field.send_keys(ENUM_ATTRIBUTE)
        driver.find_element(*SAVE_BUTTON).click()

        # Step 6: Verify ENUM attribute configured successfully
        wait.until(EC.visibility_of_element_located(INPUT_FIELD))
        config_value = enum_input_field.get_attribute('value')
        assert config_value == ENUM_ATTRIBUTE, "ENUM attribute should be correctly configured"

        # Step 7: Locate the JSON data with nested structure for viewing (FR-18)
        view_details_button = driver.find_element(By.LINK_TEXT, VIEW_DETAILS_BUTTON_TEXT)
        assert view_details_button.is_displayed(), "View Details button should be visible"

        # Step 8: Click View Details button (FR-18)
        view_details_button.click()

        # Step 9: Verify complete JSON data is displayed in modal (FR-18)
        detailed_json_modal = wait.until(EC.visibility_of_element_located(DETAILED_JSON_MODAL))
        assert detailed_json_modal.is_displayed(), "JSON data modal should be visible"

        # Step 10: Verify the displayed JSON data
        displayed_json = driver.find_element(*DETAILED_JSON_DISPLAY).text
        assert json.loads(displayed_json) == json.loads(VALID_NESTED_JSON), "Complete JSON data should be displayed accurately"

    finally:
        driver.quit()