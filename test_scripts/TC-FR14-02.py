
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_formula_drag_without_drop():
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
driver.get("http://yourapplicationurl.com/workflow-canvas")
formula_component = driver.find_element(By.XPATH, "//div[@id='formula-component']")
action_chains = webdriver.ActionChains(driver)
action_chains.click_and_hold(formula_component).perform()
time.sleep(1)
assert formula_component.is_displayed() in driver.page_source
finally:
driver.quit()
