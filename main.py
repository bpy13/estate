from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# initialize data in json
data = {} # keys: estate, tower, floor, flat, area, transactions

# setup selenium
options = Options()
url = "https://hk.centanet.com/estate/%E5%A4%AA%E5%8F%A4%E5%9F%8E/3-OVDUURFSRJ"

driver = webdriver.Chrome(options=options)
driver.get(url)


url = "https://hk.centanet.com/estate/"

# loop over estates


driver.quit()


def search_price():
    data = []
    wait = WebDriverWait(driver, 10)
    floors = driver.find_elements(By.CLASS_NAME, "floorsNumber")
    table_rows = driver.find_elements(By.CLASS_NAME, "historyTable_row")
    for floor, row in zip(floors, table_rows):
        flats = row.find_elements(By.CLASS_NAME, "nhistory_xAxis")
        for flat in flats:
            driver.execute_script("arguments[0].click();", flat)
            _ = wait.until(lambda d: d.execute_script("return jQuery.active == 0"))
            room = flat.find_element(By.CLASS_NAME, "flat")
            area_raw = driver.find_element(By.CLASS_NAME, "floorInfoArea").text
            area = area_raw.split("・")[0].split(" ")[1]
            data.append({
                "floor": floor.text,
                "flat": room.text,
                "area_raw": area_raw,
                "area": area,
                "transactions": []
            })
            print(data[-1])
            bargain_table = driver.find_element(By.CLASS_NAME, "bargainTable")
            prices = bargain_table.find_elements(By.CLASS_NAME, "bargainPrice")
            for price in prices:
                transaction = price.find_element(By.XPATH, "./ancestor::tr[1]")
                date = transaction.find_element(By.XPATH, "./td[1]")
                data[-1]["transactions"].append({
                    "date": date.text,
                    "price_raw": price.text,
                    "price": price.text[1:-1]
                })
    return data

