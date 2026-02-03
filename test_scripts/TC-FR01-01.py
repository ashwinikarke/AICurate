
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_workflow_card_click():
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
driver.get("http://yourapplicationurl.com/dashboard")
assert "Dashboard" in driver.title
driver.find_element(By.XPATH, "//div[@class='workflow-card']").click()
assert "Workflow Configuration" in driver.title
finally:
driver.quit()
