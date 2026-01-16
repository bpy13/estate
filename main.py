from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# initialize data in json

options = Options()
driver = webdriver.Chrome(options=options)

# loop over estates

url = "https://hk.centanet.com/estate/%E5%A4%AA%E5%8F%A4%E5%9F%8E/3-OVDUURFSRJ"
driver.get(url)

# loop over group, then loop over buildings

elements = driver.find_elements(By.CLASS_NAME, "nhistory_xAxis")
driver.execute_script("arguments[0].click();", elements[0])

# loop over flats

popup = driver.find_elements(By.CLASS_NAME, "floorInfoBox")
popup[0].text # get info

driver.quit()
