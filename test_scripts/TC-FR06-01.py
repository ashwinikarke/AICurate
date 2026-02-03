
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_upload_button_functionality():
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
driver.get("http://yourapplicationurl.com/workflow-config")
upload_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Upload CSV or JSON')]")
upload_button.click()
time.sleep(1)
assert driver.find_element(By.XPATH, "//input[@type='file']").is_displayed()
finally:
driver.quit()
