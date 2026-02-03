
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_no_field_selected():
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
driver.get("http://yourapplicationurl.com/workflow-config")
submit_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Submit')]")
submit_button.click()
time.sleep(1)
assert "Please select a field" in driver.page_source
finally:
driver.quit()
