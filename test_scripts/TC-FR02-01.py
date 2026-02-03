
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_input_component_present():
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
driver.get("http://yourapplicationurl.com/workflow-config")
assert "Workflow Config" in driver.title
input_component = driver.find_element(By.XPATH, "//div[@id='input-component']")
assert input_component.is_displayed()
finally:
driver.quit()
