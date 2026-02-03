
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_input_name_entry():
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
driver.get("http://yourapplicationurl.com/workflow-config")
input_name_field = driver.find_element(By.XPATH, "//input[@id='input-name']")
input_name_field.send_keys("Test Input")
time.sleep(1)
assert "Test Input" in driver.page_source
finally:
driver.quit()
