
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_rule_submission_for_review():
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
driver.get("http://yourapplicationurl.com/rule-submission")
submit_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Submit for Review')]")
submit_button.click()
time.sleep(1)
assert "Submission for review successful" in driver.page_source
finally:
driver.quit()
