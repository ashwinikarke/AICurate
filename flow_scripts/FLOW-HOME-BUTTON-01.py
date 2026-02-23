from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# CONFIGURATION 
BASE_URL = "https://app-under-test/home"
INTERACT_BUTTON = (By.ID, "interactCustomersBtn")
INTERACTION_INTERFACE = (By.ID, "customerInteractionInterface")

# ----------------------------
# TEST FLOW (EXECUTION SCRIPT)
# Covers: FR-15, FR-16, FR-19
# ----------------------------
def test_homepage_interaction():
    # WebDriver setup using WebDriverManager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    wait = WebDriverWait(driver, 10)

    try:
        # Step 1: Open Homepage (FR-15)
        driver.get(BASE_URL)

        # Step 2: Verify 'Interact with Customers' button is visible (FR-15)
        interact_button = wait.until(EC.visibility_of_element_located(INTERACT_BUTTON))
        assert interact_button.is_displayed(), "Interact with Customers button should be visible on the homepage."

        # Step 3: Click on 'Interact with Customers' button (FR-16)
        interact_button.click()

        # Step 4: Verify Customer Interaction Interface is displayed (FR-16)
        interaction_interface = wait.until(EC.visibility_of_element_located(INTERACTION_INTERFACE))
        assert interaction_interface.is_displayed(), "Customer interaction interface should be displayed successfully."

        # Step 5: Check responsiveness and accessibility of the 'Interact with Customers' button (FR-19)
        driver.set_window_size(375, 667)  # Simulate mobile device size
        driver.refresh()  # Refresh to apply the mobile view

        # Step 6: Verify 'Interact with Customers' button is still accessible (FR-19)
        interact_button_mobile = wait.until(EC.visibility_of_element_located(INTERACT_BUTTON))
        assert interact_button_mobile.is_displayed(), "Interact with Customers button should be accessible on mobile."

    finally:
        driver.quit()