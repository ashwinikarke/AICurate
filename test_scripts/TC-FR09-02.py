
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_no_delete_button_without_file():
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
driver.get("http://yourapplicationurl.com/workflow-config")
assert "Workflow Config" in driver.title
delete_buttons = driver.find_elements(By.XPATH, "//button[contains(text(), 'Delete')]")
assert len(delete_buttons) == 0
finally:
driver.quit()
