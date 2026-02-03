
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_upload_valid_json():
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
driver.get("http://yourapplicationurl.com/workflow-config")
upload_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Upload')]")
upload_button.click()
time.sleep(1)
upload_input = driver.find_element(By.XPATH, "//input[@type='file']")
upload_input.send_keys("/path/to/valid.json")
time.sleep(1)
assert "Upload Successful" in driver.page_source
finally:
driver.quit()
