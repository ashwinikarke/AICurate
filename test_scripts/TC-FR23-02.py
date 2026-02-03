
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_invalid_json_input_handling():
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
driver.get("http://yourapplicationurl.com/simulation")
json_input_field = driver.find_element(By.XPATH, "//textarea[@id='json-test-input']")
json_input_field.send_keys("{'key': 'value'}")
assert "Invalid JSON format" in driver.page_source
finally:
driver.quit()
