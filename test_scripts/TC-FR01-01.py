
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://example.com/login")
driver.find_element(By.ID, "username").send_keys("validUser")
driver.find_element(By.ID, "password").send_keys("validPassword")
driver.find_element(By.ID, "loginButton").click()
assert "Dashboard" in driver.title
driver.quit()