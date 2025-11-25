
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def test_sso_login():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        # Step 1: Navigate to login page
        driver.get("http://example.com/login")
        # Step 2: Click 'Login with SSO'
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Login with SSO']"))).click()
        # Step 3: Enter username
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "username"))).send_keys("testuser")
        # Step 4: Enter password
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys("password123")
        # Step 5: Click 'Sign In'
        driver.find_element(By.XPATH, "//button[text()='Sign In']").click()
        # Assertion for success
        assert "Dashboard" in driver.title
        print("Login successful.")
    except Exception as e:
        print(f"Failed: {e}")
    finally:
        driver.quit()
test_sso_login()