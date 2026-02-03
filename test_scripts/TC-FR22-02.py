
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_execute_workflow_no_permission():
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
driver.get("http://yourapplicationurl.com/workflow-config")
execute_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Execute Workflow')]")
execute_button.click()
time.sleep(1)
assert "Access Denied" in driver.page_source
finally:
driver.quit()
