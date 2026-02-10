from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# CONFIGURATION 
BASE_URL = "https://platform-under-test"
CHAT_MESSAGE = "Hello! Need assistance."
INCOMPLETE_QUESTIONNAIRE = "Incomplete response"
MAX_INPUT = "X" * 1000  # Assuming 1000 is the max character length

# Locators (adjust per application)
CHAT_INPUT = (By.ID, "chatInput")
SEND_BUTTON = (By.ID, "sendMessageBtn")
ERROR_MESSAGE = (By.CLASS_NAME, "error-message")
NEEDS_ASSESSMENT_LINK = (By.LINK_TEXT, "Needs Assessment")
NEEDS_ASSESSMENT_PAGE = (By.ID, "needsAssessmentPage")
QUESTIONNAIRE_INPUT = (By.ID, "questionnaireInput")
SUBMIT_BUTTON = (By.ID, "submitAssessmentBtn")
CONFIRMATION_MESSAGE = (By.CLASS_NAME, "confirmation-message")
REQUIRED_FIELD_ERROR = (By.CLASS_NAME, "required-field-error")

# ----------------------------
# TEST FLOW (EXECUTION SCRIPT)
# Covers: FR-01 → FR-02
# ----------------------------
def test_customer_interaction_and_needs_assessment_flow():
    # WebDriver setup using WebDriverManager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    wait = WebDriverWait(driver, 10)

    try:
        # Step 1: Navigate to the platform URL (FR-01)
        driver.get(BASE_URL)

        # Step 2: Check for interaction elements (chat, feedback) (FR-01)
        chat_input = wait.until(EC.visibility_of_element_located(CHAT_INPUT))
        assert chat_input.is_displayed(), "Chat input should be visible"
        send_button = driver.find_element(*SEND_BUTTON)
        assert send_button.is_displayed(), "Send button should be visible"

        # Step 3: Attempt to send a message without logging in (FR-01)
        send_button.click()
        error_message = wait.until(EC.visibility_of_element_located(ERROR_MESSAGE))
        assert "please log in" in error_message.text.lower(), "Login error message should be displayed"

        # Step 4: Navigate to needs assessment (FR-02)
        driver.find_element(*NEEDS_ASSESSMENT_LINK).click()
        wait.until(EC.visibility_of_element_located(NEEDS_ASSESSMENT_PAGE))

        # Step 5: Submit without completing required fields (FR-02)
        driver.find_element(*SUBMIT_BUTTON).click()
        required_error = wait.until(EC.visibility_of_element_located(REQUIRED_FIELD_ERROR))
        assert "fill out required fields" in required_error.text.lower(), "Required fields error should be displayed"

        # Step 6: Complete the questionnaire with maximum boundary input (FR-02)
        questionnaire_input = driver.find_element(*QUESTIONNAIRE_INPUT)
        questionnaire_input.send_keys(MAX_INPUT)
        driver.find_element(*SUBMIT_BUTTON).click()

        # Step 7: Confirm submission success message
        confirmation = wait.until(EC.visibility_of_element_located(CONFIRMATION_MESSAGE))
        assert "successfully assessed" in confirmation.text.lower(), "Confirmation message should appear"

    finally:
        driver.quit()

# Run the test flow
if __name__ == "__main__":
    test_customer_interaction_and_needs_assessment_flow()


In this script, we cover the end-to-end flow for customer interaction and needs assessment by incorporating both positive and negative paths. Starting from checking the chat interface accessibility to validating the needs assessment feature, including response validation, the script accurately reflects the specified requirements and necessary assertions.