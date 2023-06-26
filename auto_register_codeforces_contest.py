from quick_message import *
from config import(
    line_bot_api,
    CODEFORCES_CLASS
)
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait   
from selenium.webdriver.support import expected_conditions as EC

from linebot.models import (
    MessageEvent,
    TextMessage, 
    TextSendMessage
)

# AUTO_REGISTER_CODEFORCES_CONTEST

def REGISTER_CODEFORCES_CONTEST(reply_token_copy, ACCOUNT, PASSWORD):
    print("CODEFORCES_CONTEST_REGISTER_URL", CODEFORCES_CLASS.CONTEST_REGISTER_URL)
    Chromeoptions = Options()
    Chromeoptions.add_argument('--headless')
    s = Service('./chromedriver')
    driver = webdriver.Chrome(service=s, options=Chromeoptions)

    driver.get(CODEFORCES_CLASS.CONTEST_REGISTER_URL)

    # Sign in account
    account_box = driver.find_element(By.XPATH, "//input[@id='handleOrEmail']")
    password_box = driver.find_element(By.XPATH, "//input[@id='password']")
    login_button = driver.find_element(By.XPATH, "//input[@value='Login']")

    account_box.send_keys(ACCOUNT)
    password_box.send_keys(PASSWORD)
    login_button.click()

    def find_register_button():
        try:
            button = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//input[@value='Register']"))
            )
            return button

        except:
            return -1

    Register_button = find_register_button()

    if type(Register_button) != int:
        Register_button.click()
        driver.close()
        line_bot_api.reply_message(
            reply_token_copy,
            TextSendMessage(text="Successful Registered", quick_reply=QUICK_MESSAGE_BUTTON)
        )

    else: 
        line_bot_api.reply_message(
            reply_token_copy,
            TextSendMessage(text="Registered Alreadey", quick_reply=QUICK_MESSAGE_BUTTON)
        )

    return