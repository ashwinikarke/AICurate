
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
import time
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://example.com/login")
driver.find_element(By.ID, "loginButton").click()
error_message = driver.find_element(By.ID, "error").text
assert error_message == "Fields cannot be empty"
driver.quit()