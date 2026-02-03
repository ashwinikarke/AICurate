
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_file_deletion():
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
driver.get("http://yourapplicationurl.com/workflow-config")
upload_input = driver.find_element(By.XPATH, "//input[@type='file']")
upload_input.send_keys("/path/to/file.json")
time.sleep(1)
delete_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Delete')]")
delete_button.click()
time.sleep(1)
assert "File deleted successfully" in driver.page_source
finally:
driver.quit()
