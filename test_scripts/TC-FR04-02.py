
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://example.com/workflows/execution")
driver.find_element(By.ID, "inputField").send_keys("invalidJSON")
driver.find_element(By.ID, "submitButton").click()
error_message = driver.find_element(By.ID, "error").text
assert error_message == "Invalid JSON format"
driver.quit()