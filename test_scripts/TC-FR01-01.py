
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_successful_login():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get('http://example.com/login')
        assert 'Login' in driver.title
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'username'))
        ).send_keys('validUser')
        driver.find_element(By.NAME, 'password').send_keys('validPass')
        driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]").click()
        WebDriverWait(driver, 10).until(
            EC.url_contains('/dashboard')
        )
        assert 'Dashboard' in driver.title
        print("Login successful.")
    except Exception as e:
        print(f"Login failed: {e}")
    finally:
        driver.quit()
test_successful_login()