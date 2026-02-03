
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_submit_to_database():
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
driver.get("http://yourapplicationurl.com/configure")
input_field = driver.find_element(By.XPATH, "//input[@id='config-name']")
input_field.send_keys("Configuration Test")
submit_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Submit')]")
submit_button.click()
time.sleep(1)
assert "Configuration saved to DB" in driver.page_source
finally:
driver.quit()
