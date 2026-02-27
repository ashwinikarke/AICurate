from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# CONFIGURATION 
BASE_URL = "https://customer-interaction-platform.com"
NEED_IDENTIFICATION_URL = "https://customer-interaction-platform.com/identify-needs"
INVALID_DATA = "@@@"

# Locators (adjust per application)
CHAT_FEATURE = (By.ID, "chatFeature")
CONTACT_FORM = (By.ID, "contactForm")
ACCESS_DENIED_MESSAGE = (By.CLASS_NAME, "access-denied")
IDENTIFY_NEEDS_BUTTON = (By.ID, "identifyNeedsBtn")
FEEDBACK_INPUT = (By.ID, "feedbackInput")
IDENTIFIED_NEEDS_OUTPUT = (By.ID, "identifiedNeeds")
INVALID_INPUT_MESSAGE = (By.CLASS_NAME, "error-message")

# ----------------------------
# TEST FLOW (EXECUTION SCRIPT)
# Covers: FR-01 → FR-02
# ----------------------------
def test_customer_interaction_and_needs_identification():
    # WebDriver setup using WebDriverManager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    wait = WebDriverWait(driver, 10)

    try:
        # Step 1: Open Customer Interaction Platform (FR-01)
        driver.get(BASE_URL)
        
        # Step 2: Verify the platform loads successfully
        wait.until(EC.visibility_of_element_located(CHAT_FEATURE))
        assert driver.find_element(*CHAT_FEATURE).is_displayed(), "Chat feature should be visible"
        assert driver.find_element(*CONTACT_FORM).is_displayed(), "Contact form should be visible"

        # Step 3: Verify interaction elements with no permissions (FR-01)
        driver.get(BASE_URL + "/unauthorized-access")
        error_message = wait.until(EC.visibility_of_element_located(ACCESS_DENIED_MESSAGE))
        assert "access denied" in error_message.text.lower(), "Access denied message should be visible"

        # Step 4: Attempt to use chat feature without logging in (FR-01)
        driver.get(BASE_URL)
        chat_feature = driver.find_element(*CHAT_FEATURE)
        chat_feature.click()
        assert "Please log in." in wait.until(EC.visibility_of_element_located(ACCESS_DENIED_MESSAGE)).text, "Chat feature should prompt for login"

        # Step 5: Navigate to need identification feature (FR-02)
        driver.get(NEED_IDENTIFICATION_URL)
        wait.until(EC.visibility_of_element_located(IDENTIFY_NEEDS_BUTTON))

        # Step 6: Enter valid customer feedback data (FR-02)
        feedback_input = driver.find_element(*FEEDBACK_INPUT)
        feedback_input.send_keys("I need assistance with my order.")
        driver.find_element(*IDENTIFY_NEEDS_BUTTON).click()
        identified_needs = wait.until(EC.visibility_of_element_located(IDENTIFIED_NEEDS_OUTPUT))
        assert identified_needs.is_displayed(), "Identified needs should be displayed"

        # Step 7: Enter invalid data for need identification (FR-02)
        feedback_input.clear()
        feedback_input.send_keys(INVALID_DATA)
        driver.find_element(*IDENTIFY_NEEDS_BUTTON).click()
        invalid_input_message = wait.until(EC.visibility_of_element_located(INVALID_INPUT_MESSAGE))
        assert "invalid input" in invalid_input_message.text.lower(), "Invalid input error message should be visible"

    finally:
        driver.quit()