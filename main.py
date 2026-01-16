from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
driver = webdriver.Chrome(options=options)
url = "https://hk.centanet.com/estate/%E5%A4%AA%E5%8F%A4%E5%9F%8E/3-OVDUURFSRJ"
driver.get(url)
time.sleep(3)  # Wait for page to load
elements = driver.find_elements(By.CLASS_NAME, "nhistory_xAxis")
if elements:
    elements[0].click()
    print("Clicked first element!")
else:
    print("No elements found!")


driver.quit()
