
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_disabled_workflow_card():
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
driver.get("http://yourapplicationurl.com/dashboard")
assert "Dashboard" in driver.title
disabled_card = driver.find_element(By.XPATH, "//div[@class='workflow-card disabled']")
assert not disabled_card.is_enabled() # Clicking won't work
disabled_card.click() # Attempt to click
assert "Dashboard" in driver.title
finally:
driver.quit()
