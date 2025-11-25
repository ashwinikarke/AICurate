
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def sso_login_invalid(url, username, password):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Login with SSO')]"))
        ).click()
        time.sleep(2)
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "i0116"))).send_keys(username)
        driver.find_element(By.ID, "idSIButton9").click()
        time.sleep(2)
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "i0118"))).send_keys(password)
        driver.find_element(By.ID, "idSIButton9").click()
        time.sleep(2)
        error_message = driver.find_element(By.ID, "errorElement").text
        assert error_message == "Invalid credentials"
        print("Error message displayed as expected.")
    except Exception as e:
        print(f"Login failed: {e}")
    finally:
        driver.quit()
sso_login_invalid('http://example.com', 'wronguser', 'wrongpass')
