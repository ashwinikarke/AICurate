
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_call_workflow_drag_and_drop():
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
driver.get("http://yourapplicationurl.com/workflow-canvas")
call_workflow_component = driver.find_element(By.XPATH, "//div[@id='call-workflow-component']")
canvas_area = driver.find_element(By.XPATH, "//div[@id='canvas-area']")
driver.execute_script("arguments[0].scrollIntoView();", call_workflow_component)
action_chains = webdriver.ActionChains(driver)
action_chains.drag_and_drop(call_workflow_component, canvas_area).perform()
time.sleep(1)
assert call_workflow_component.is_displayed() in driver.page_source
finally:
driver.quit()
