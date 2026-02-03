
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_drag_and_drop_upload():
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
driver.get("http://yourapplicationurl.com/workflow-config")
upload_area = driver.find_element(By.XPATH, "//div[@id='upload-area']")
# Simulate drag and drop
driver.execute_script("var dataTransfer = new DataTransfer(); dataTransfer.items.add(new File(['test'], 'test.json'));")
upload_area.send_keys("/path/to/test.json")
time.sleep(1)
assert "Upload Successful" in driver.page_source
finally:
driver.quit()
