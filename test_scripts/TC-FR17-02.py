
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_call_workflow_drag_without_drop():
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
driver.get("http://yourapplicationurl.com/workflow-canvas")
call_workflow_component = driver.find_element(By.XPATH, "//div[@id='call-workflow-component']")
action_chains = webdriver.ActionChains(driver)
action_chains.click_and_hold(call_workflow_component).perform()
time.sleep(1)
assert call_workflow_component.is_displayed() in driver.page_source
finally:
driver.quit()
