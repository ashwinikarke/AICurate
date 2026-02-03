
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_input_reference_key_submission():
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
driver.get("http://yourapplicationurl.com/workflow-config")
ref_key_field = driver.find_element(By.XPATH, "//input[@id='input-ref-key']")
ref_key_field.send_keys("referenceKey")
submit_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Submit')]")
submit_button.click()
time.sleep(1)
assert "Submission successful" in driver.page_source
finally:
driver.quit()
