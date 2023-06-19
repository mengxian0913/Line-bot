from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os, time
Chromeoptions = Options()
# Chromeoptions.add_argument('--headless')
s = Service('./chromedriver')
driver = webdriver.Chrome(service=s, options=Chromeoptions)

YOURACOUNT = "vincent0913"
YOURPASSWORD = "vincent09132362"

CODEFORCES_REGISTER_URL = "https://codeforces.com/enter?back=%2FcontestRegistration%2F1843"
driver.get(CODEFORCES_REGISTER_URL)
# Sign in account

account_box = driver.find_element(By.XPATH, "//input[@id='handleOrEmail']")
password_box = driver.find_element(By.XPATH, "//input[@id='password']")
login_button = driver.find_element(By.XPATH, "//input[@value='Login']")

account_box.send_keys(YOURACOUNT)
password_box.send_keys(YOURPASSWORD)
login_button.click()
ok = 1

def find_register_button():
    global ok
    try:
        button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//input[@value='Register']"))
        )
        return button

    except:
        ok = 0
        return 123

Register_button = find_register_button()

if ok:
    Register_button.click()

else: 
    print("already register")

time.sleep(10)

driver.close()
