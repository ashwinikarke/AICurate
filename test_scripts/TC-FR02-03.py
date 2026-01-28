
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://example.com/workflows")
driver.find_element(By.ID, "searchButton").click()
message = driver.find_element(By.ID, "emptySearch").text
assert message == "Please enter a search term"
driver.quit()