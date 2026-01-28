
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://example.com/workflows")
assert driver.find_element(By.ID, "draftTab").is_displayed()
assert driver.find_element(By.ID, "reviewTab").is_displayed()
assert driver.find_element(By.ID, "publishedTab").is_displayed()
driver.quit()