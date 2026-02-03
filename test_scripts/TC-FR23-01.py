
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_json_input_field_presence():
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
driver.get("http://yourapplicationurl.com/simulation")
json_input_field = driver.find_element(By.XPATH, "//textarea[@id='json-test-input']")
assert json_input_field.is_displayed()
finally:
driver.quit()
