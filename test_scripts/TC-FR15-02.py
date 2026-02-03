
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_successful_formula_submission():
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
driver.get("http://yourapplicationurl.com/formula-config")
formula_field = driver.find_element(By.XPATH, "//textarea[@id='formula-input']")
formula_field.send_keys("x + y")
submit_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Submit')]")
submit_button.click()
time.sleep(1)
assert "Formula submitted successfully" in driver.page_source
finally:
driver.quit()
