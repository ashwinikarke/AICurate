
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://example.com/workflows/published/nonExistingWorkflow")
error_message = driver.find_element(By.ID, "notFound").text
assert error_message == "Workflow not found"
driver.quit()