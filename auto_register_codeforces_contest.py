from detect import (
    CODEFORCES_CLASS
)
from config import line_bot_api, handler
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

def REGISTER_CODEFORCES_CONTEST(reply_token_copy):
    print("CODEFORCES_CONTEST_REGISTER_URL", CODEFORCES_CLASS.CODEFORCES_CONTEST_REGISTER_URL)
    Chromeoptions = Options()
    Chromeoptions.add_argument('--headless')
    s = Service('./chromedriver')
    driver = webdriver.Chrome(service=s, options=Chromeoptions)

    YOURACOUNT = "exo930122@gmail.com"
    YOURPASSWORD = "vincent09132362"

    driver.get(CODEFORCES_CLASS.CODEFORCES_CONTEST_REGISTER_URL)

    # Sign in account
    account_box = driver.find_element(By.XPATH, "//input[@id='handleOrEmail']")
    password_box = driver.find_element(By.XPATH, "//input[@id='password']")
    login_button = driver.find_element(By.XPATH, "//input[@value='Login']")

    account_box.send_keys(YOURACOUNT)
    password_box.send_keys(YOURPASSWORD)
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
            TextSendMessage(text="Successful Register")
        )

    else: 
        line_bot_api.reply_message(
            reply_token_copy,
            TextSendMessage(text="Register Alreadey")
        )

    return