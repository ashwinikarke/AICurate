
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_no_edit_option():
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
driver.get("http://yourapplicationurl.com/drafts")
edit_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Edit')]")
assert not edit_button.is_displayed()
finally:
driver.quit()
