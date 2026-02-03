
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_generate_schema_without_upload():
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
driver.get("http://yourapplicationurl.com/workflow-config")
generate_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Generate schema')]")
generate_button.click()
time.sleep(1)
assert "File upload is required" in driver.page_source
finally:
driver.quit()
