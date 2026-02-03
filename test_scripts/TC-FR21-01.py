
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_rule_editability():
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
driver.get("http://yourapplicationurl.com/drafts")
edit_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Edit')]")
edit_button.click()
time.sleep(1)
assert "Editing Rule" in driver.title
finally:
driver.quit()
