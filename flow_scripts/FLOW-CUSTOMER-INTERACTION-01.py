from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# CONFIGURATION 
BASE_URL = "https://app-under-test/home"
CHAT_BUTTON = (By.ID, "startChatBtn")
CHAT_WINDOW = (By.ID, "chatWindow")
MESSAGE_INPUT = (By.ID, "messageInput")
SEND_BUTTON = (By.ID, "sendBtn")
WELCOME_MESSAGE = (By.ID, "welcomeMsg")
CHAT_OPTIONS = (By.CLASS_NAME, "chat-options")

# ----------------------------
# TEST FLOW (EXECUTION SCRIPT)
# Covers: FR-03 to FR-07
# ----------------------------
def test_customer_interaction_workflow():
    # WebDriver setup using WebDriverManager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    wait = WebDriverWait(driver, 10)

    try:
        # Step 1: Navigate to Home Page (FR-03)
        driver.get(BASE_URL)

        # Step 2: Verify welcome message is loaded (FR-04)
        assert wait.until(EC.visibility_of_element_located(WELCOME_MESSAGE)).is_displayed(), "Welcome message should be displayed"

        # Step 3: Check availability of chat options (FR-05)
        chat_options = wait.until(EC.visibility_of_element_located(CHAT_OPTIONS))
        assert chat_options.is_displayed(), "Chat options should be visible on the platform"

        # Step 4: Click on ‘Start Chat’ button to open chat window (FR-06)
        driver.find_element(*CHAT_BUTTON).click()
        chat_window = wait.until(EC.visibility_of_element_located(CHAT_WINDOW))
        assert chat_window.is_displayed(), "Chat window should open successfully"

        # Step 5: Send a message through chat (FR-07)
        message_input = driver.find_element(*MESSAGE_INPUT)
        message_input.send_keys("Hello")
        driver.find_element(*SEND_BUTTON).click()

        # Step 6: Verify that message appears in the chat (FR-07)
        # Here we need a logic to verify if the message is sent. This may require catching UI behavior.
        assert "Hello" in chat_window.text, "Message 'Hello' should be sent successfully"

    finally:
        driver.quit()