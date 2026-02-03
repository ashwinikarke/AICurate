
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_template_download():
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
driver.get("http://yourapplicationurl.com/workflow-config")
download_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Download Template')]")
download_button.click()
time.sleep(3)
assert "Template.xlsx" in driver.get_downloads()
finally:
driver.quit()
