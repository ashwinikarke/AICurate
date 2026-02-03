
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_input_reference_key_presence():
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
driver.get("http://yourapplicationurl.com/workflow-config")
ref_key_field = driver.find_element(By.XPATH, "//input[@id='input-ref-key']")
assert ref_key_field.is_displayed()
finally:
driver.quit()
