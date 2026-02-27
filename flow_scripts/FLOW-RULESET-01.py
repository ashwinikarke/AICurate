from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# CONFIGURATION 
BASE_URL = "https://app-under-test/ruleset-config"
RULESET_COMPONENT = (By.ID, "rulesetComponent")
CANVAS = (By.ID, "canvas")
CONFIRMATION_MESSAGE = (By.CLASS_NAME, "confirmation")
RULESET_FIELD = (By.ID, "rulesetField")
SUBMIT_BUTTON = (By.ID, "submitBtn")

# ----------------------------
# TEST FLOW (EXECUTION SCRIPT)
# Covers: FR-29, FR-30, FR-36
# ----------------------------
def test_ruleset_configuration_flow():
    # WebDriver setup using WebDriverManager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    wait = WebDriverWait(driver, 10)

    try:
        # Step 1: Open Ruleset Configuration Page (FR-29)
        driver.get(BASE_URL)

        # Step 2: Verify sidebar is displayed (FR-29)
        wait.until(EC.visibility_of_element_located(RULESET_COMPONENT))

        # Step 3: Drag Ruleset component to canvas
        ruleset_component = driver.find_element(*RULESET_COMPONENT)
        canvas = driver.find_element(*CANVAS)
        
        actions = webdriver.ActionChains(driver)
        actions.click_and_hold(ruleset_component).move_to_element(canvas).release().perform()
        time.sleep(1)  # wait for the drop action to complete
        
        # Step 4: Verify Ruleset component dropped successfully
        assert canvas.find_element(*RULESET_COMPONENT).is_displayed(), \
            "Ruleset component should be successfully dropped onto the canvas"

        # Step 5: Verify Ruleset field is present and marked as required (FR-30)
        ruleset_field = wait.until(EC.visibility_of_element_located(RULESET_FIELD))
        assert "required" in ruleset_field.get_attribute("class"), \
            "Ruleset field should be marked as required"

        # Step 6: Enter a valid value in Ruleset field
        ruleset_field.send_keys("Valid Ruleset Config")

        # Step 7: Click Submit button (FR-36)
        submit_btn = driver.find_element(*SUBMIT_BUTTON)
        submit_btn.click()

        # Step 8: Verify submission confirmation message (FR-36)
        confirmation = wait.until(EC.visibility_of_element_located(CONFIRMATION_MESSAGE))
        assert "success" in confirmation.text.lower(), \
            "Confirmation message should indicate successful configuration save"

    finally:
        driver.quit()