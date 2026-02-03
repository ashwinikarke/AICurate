
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_invalid_nested_json_input():
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
driver.get("http://yourapplicationurl.com/workflow-config")
input_field = driver.find_element(By.XPATH, "//textarea[@id='json-input']")
invalid_nested_json = '{"key1": {"key2": value}}'
input_field.send_keys(invalid_nested_json)
assert "Invalid JSON" in driver.page_source
finally:
driver.quit()
