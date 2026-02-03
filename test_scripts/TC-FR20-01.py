
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_draft_list_elements():
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
driver.get("http://yourapplicationurl.com/drafts")
assert "Drafts" in driver.title
assert driver.find_element(By.XPATH, "//th[contains(text(), 'Rule Name')]").is_displayed()
assert driver.find_element(By.XPATH, "//th[contains(text(), 'Description')]").is_displayed()
assert driver.find_element(By.XPATH, "//th[contains(text(), 'Version')]").is_displayed()
assert driver.find_element(By.XPATH, "//th[contains(text(), 'Modified By')]").is_displayed()
finally:
driver.quit()
