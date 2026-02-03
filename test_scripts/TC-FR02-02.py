
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_input_component_absent():
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
driver.get("http://yourapplicationurl.com/other-page")
assert "Other Page" in driver.title
assert not driver.find_elements(By.XPATH, "//div[@id='input-component']")
finally:
driver.quit()
