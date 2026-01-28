
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://example.com/workflows/published/workflowDetails")
driver.find_element(By.ID, "executeButton").click()
success_message = driver.find_element(By.ID, "successMessage").text
assert success_message == "Workflow executed successfully"
driver.quit()