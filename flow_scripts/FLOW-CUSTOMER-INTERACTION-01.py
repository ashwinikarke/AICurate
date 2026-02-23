from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# CONFIGURATION 
BASE_URL = "https://platform-under-test/"
INVALID_EMAIL = "invalid.user@test.com"
INVALID_PASSWORD = "Wrong@123"
VALID_EMAIL = "valid.user@test.com"
VALID_PASSWORD = "Valid@123"

# Locators (adjust per application)
INTERACT_BUTTON = (By.ID, "interactCustomersBtn")
LOGIN_BUTTON = (By.ID, "loginBtn")
EMAIL_INPUT = (By.ID, "email")
PASSWORD_INPUT = (By.ID, "password")
ERROR_MESSAGE = (By.CLASS_NAME, "error-message")
RECOMMENDATIONS_PAGE = (By.ID, "recommendationsPage")
NEEDS_INPUT = (By.ID, "needsInput")
SUBMIT_BUTTON = (By.ID, "submitNeeds")
RECOMMENDATIONS_OUTPUT = (By.CLASS_NAME, "recommendation-output")

# ----------------------------
# TEST FLOW (EXECUTION SCRIPT)
# Covers: FR-01, FR-02
# ----------------------------
def test_customer_interaction_and_needs_identification_flow():
    # WebDriver setup using WebDriverManager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    wait = WebDriverWait(driver, 10)

    try:
        # Step 1: Navigate to the platform URL
        driver.get(BASE_URL)

        # Step 2: Check if the Interact with Customers button is displayed (FR-01)
        interact_btn = wait.until(EC.visibility_of_element_located(INTERACT_BUTTON))
        assert interact_btn.is_displayed(), "Interact with Customers button should be displayed"

        # Step 3: Click 'Interact with Customers' button (FR-01)
        interact_btn.click()

        # Step 4: Verify user is redirected to the login page when not logged in (FR-01)
        wait.until(EC.url_contains("login"))
        
        # Step 5: Enter invalid login credentials (FR-02)
        driver.find_element(*EMAIL_INPUT).send_keys(INVALID_EMAIL)
        driver.find_element(*PASSWORD_INPUT).send_keys(INVALID_PASSWORD)
        driver.find_element(*LOGIN_BUTTON).click()

        # Step 6: Verify error message appears when invalid credentials are used (FR-02)
        error_message = wait.until(EC.visibility_of_element_located(ERROR_MESSAGE))
        assert "invalid" in error_message.text.lower(), "Error message for invalid credentials should be displayed"

        # Step 7: Log in with valid credentials for further tests (FR-01, FR-02)
        driver.find_element(*EMAIL_INPUT).clear()
        driver.find_element(*EMAIL_INPUT).send_keys(VALID_EMAIL)
        driver.find_element(*PASSWORD_INPUT).clear()
        driver.find_element(*PASSWORD_INPUT).send_keys(VALID_PASSWORD)
        driver.find_element(*LOGIN_BUTTON).click()

        # Step 8: Navigate to Recommendations Page (FR-02)
        wait.until(EC.visibility_of_element_located(RECOMMENDATIONS_PAGE))
        driver.get(BASE_URL + "recommendations")

        # Step 9: Provide needs input and submit (FR-02)
        needs_input_field = wait.until(EC.visibility_of_element_located(NEEDS_INPUT))
        needs_input_field.send_keys("I need better support")
        driver.find_element(*SUBMIT_BUTTON).click()

        # Step 10: Check if recommendations are generated (FR-02)
        recommendations = wait.until(EC.visibility_of_element_located(RECOMMENDATIONS_OUTPUT))
        assert recommendations.is_displayed(), "Recommendations based on needs should be displayed"

        # Step 11: Provide no input and submit (FR-02)
        needs_input_field.clear()
        driver.find_element(*SUBMIT_BUTTON).click()

        # Step 12: Verify error message for empty input (FR-02)
        error_message = wait.until(EC.visibility_of_element_located(ERROR_MESSAGE))
        assert "please enter your needs" in error_message.text.lower(), "Error message for empty input should appear"

        # Step 13: Provide vague input and submit (FR-02)
        needs_input_field.clear()
        needs_input_field.send_keys("I need something better")
        driver.find_element(*SUBMIT_BUTTON).click()

        # Step 14: Verify prompt for clearer input (FR-02)
        error_message = wait.until(EC.visibility_of_element_located(ERROR_MESSAGE))
        assert "clarify" in error_message.text.lower(), "Prompt for clarification on needs should be displayed"

    finally:
        driver.quit()