
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://example.com/workflows/execution")
driver.find_element(By.ID, "inputField").send_keys("{\"key\": \"value\"}")
driver.find_element(By.ID, "submitButton").click()
results_message = driver.find_element(By.ID, "results").text
assert "Execution successful" in results_message
driver.quit()