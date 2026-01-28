
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://example.com/workflows/published")
driver.find_element(By.XPATH, "//div[contains(text(), 'Published Workflow')]").click()
assert driver.find_element(By.ID, "workflowDetails").is_displayed()
driver.quit()