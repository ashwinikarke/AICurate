from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# CONFIGURATION 
BASE_URL = "https://app-under-test/login"
VALID_USERNAME = "valid.user@test.com"
INVALID_USERNAME = "invalid.user@test.com"
VALID_PASSWORD = "Valid@123"
INVALID_PASSWORD = "Wrong@123"

# Locators (adjust per application)
USERNAME_INPUT = (By.ID, "username")
PASSWORD_INPUT = (By.ID, "password")
LOGIN_BUTTON = (By.ID, "loginBtn")
ERROR_TOAST = (By.CLASS_NAME, "toast-error")
DASHBOARD_INDICATOR = (By.ID, "dashboard")

# ----------------------------
# TEST FLOW (EXECUTION SCRIPT)
# Covers: FR-01 → FR-18
# ----------------------------
def test_user_login_and_password_recovery_flow():
    # WebDriver setup using WebDriverManager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    wait = WebDriverWait(driver, 10)

    try:
        # Step 1: Open Login Page (FR-01)
        driver.get(BASE_URL)

        username_field = wait.until(EC.visibility_of_element_located(USERNAME_INPUT))
        password_field = driver.find_element(*PASSWORD_INPUT)
        login_btn = driver.find_element(*LOGIN_BUTTON)

        # Step 2: Attempt login with invalid credentials (FR-18)
        username_field.send_keys(INVALID_USERNAME)
        password_field.send_keys(INVALID_PASSWORD)
        login_btn.click()
        error = wait.until(EC.visibility_of_element_located(ERROR_TOAST))
        assert "invalid" in error.text.lower(), "Error message for invalid credentials should appear"

        # Step 3: Attempt login with valid credentials (FR-01)
        username_field.clear()
        password_field.clear()
        username_field.send_keys(VALID_USERNAME)
        password_field.send_keys(VALID_PASSWORD)
        login_btn.click()

        # Step 4: Verify dashboard redirection on successful login (FR-02)
        wait.until(EC.visibility_of_element_located(DASHBOARD_INDICATOR))

        # Step 5: Navigate back to Login page (FR-17)
        driver.get(BASE_URL)

        # Step 6: Attempt again with invalid credentials (FR-02)
        username_field.clear()
        password_field.clear()
        username_field.send_keys(INVALID_USERNAME)
        password_field.send_keys(INVALID_PASSWORD)
        login_btn.click()
        error = wait.until(EC.visibility_of_element_located(ERROR_TOAST))
        assert "invalid" in error.text.lower(), "Error message for invalid credentials should appear again"

    finally:
        driver.quit()