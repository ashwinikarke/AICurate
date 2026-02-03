
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_error_message_not_green():
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
driver.get("http://yourapplicationurl.com/workflow-config")
upload_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Upload CSV or JSON')]")
upload_button.click()
time.sleep(1)
upload_input = driver.find_element(By.XPATH, "//input[@type='file']")
upload_input.send_keys("/path/to/invalid_file.txt")
time.sleep(1)
assert not driver.find_elements(By.XPATH, "//div[@class='toast success']")
finally:
driver.quit()
