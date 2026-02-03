
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_output_field_selection():
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
driver.get("http://yourapplicationurl.com/workflow-config")
field_selection = driver.find_element(By.XPATH, "//select[@id='output-field']")
field_selection.click()
option = driver.find_element(By.XPATH, "//option[@value='outputField1']")
option.click()
assert "Field selected" in driver.page_source
finally:
driver.quit()
