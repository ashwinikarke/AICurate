
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_invalid_login():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get('http://example.com/login')
        assert 'Login' in driver.title
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'username'))
        ).send_keys('invalidUser')
        driver.find_element(By.NAME, 'password').send_keys('wrongPass')
        driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]").click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='error-message']"))
        )
        error_message = driver.find_element(By.XPATH, "//div[@class='error-message']").text
        assert error_message == "Invalid credentials"
        print("Error message displayed for invalid login.")
    except Exception as e:
        print(f"Login failed: {e}")
    finally:
        driver.quit()
test_invalid_login()