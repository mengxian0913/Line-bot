from config import line_bot_api, handler
from linebot import (
    LineBotApi,
    WebhookHandler
)
from linebot.exceptions import InvalidSignatureError
from linebot.models import (
    MessageEvent,
    TextMessage, 
    TextSendMessage
)
import time
from flask import (
    Flask,
    request, 
    abort
)
import requests
from bs4 import BeautifulSoup as bs



# AUTO_DETECT
IECS_NEWS = ""
CODEFORCES_CONTEST_NEWS = ""
DETECT_START = 0

class CODEFORCES_CONTEST_CLASS:
    ASK_STATE = 0
    CODEFORCES_CONTEST_REGISTER_URL = ""

CODEFORCES_CLASS = CODEFORCES_CONTEST_CLASS()

def DETECT_NEWS():
    global IECS_NEWS
    global CODEFORCES_CONTEST_NEWS
    global CODEFORCES_CLASS

    while True:
        try:
            CURRENT_NEWS = Get_News()
            # print(CURRENT_NEWS)
            if IECS_NEWS != CURRENT_NEWS:
                IECS_NEWS = CURRENT_NEWS
                line_bot_api.broadcast(
                    TextSendMessage(text="@Vincent 資訊系新消息!!\n"+IECS_NEWS)
                )

            CURRENT_NEWS = CODEFORCES_CONTEST()
            # print(CURRENT_NEWS)
            if CODEFORCES_CONTEST_NEWS != CURRENT_NEWS:
                CODEFORCES_CLASS.ASK_STATE = 1
                CODEFORCES_CONTEST_NEWS = CURRENT_NEWS
                line_bot_api.broadcast(
                    TextSendMessage(text="@Vincent Codeforces!!\n"+CODEFORCES_CONTEST_NEWS)
                )

        except:
            break
            
        time.sleep(3600)
    return

##############################################################################

# ALL NEWS ABOUT IECS

IECS_NEWS_URL = "https://www.iecs.fcu.edu.tw/news/"
FCU_URL = "https://www.iecs.fcu.edu.tw"
FIRST_SEARCH = 1

def Get_News():

    response = requests.get(IECS_NEWS_URL)
    soup = bs(response.text, "html.parser")
    post = soup.find(class_="post")

    post_title = post.find("a")
    post_title = post_title.get("href")
    # post_image = post.find_all("img")
    # post_image = FCU_URL + post_image[1].get("src")
    post_date = post.find("span", class_="day")
    post_month = post.find("span", class_="month")
    post_date = [post_date.text, post_month.text]
    post_link = IECS_NEWS_URL + post_title

    output = f"Title:   {post_title}\nLink:   {post_link}\nDate:   {post_date[1] + '/' + post_date[0]}\n"
    return output

##############################################################################
# Codeforces contest

CODEFORCES_URL = "https://codeforces.com"
CODEFORCES_CONTEST_URL = "https://codeforces.com/contests"

def CODEFORCES_CONTEST():
    global CODEFORCES_CLASS
    response = requests.get(CODEFORCES_CONTEST_URL)
    soup = bs(response.text, "html.parser")
    contest = soup.select_one("tr[data-contestid]")
    contest_info = contest.find_all("td")
    contest_title = contest_info[0].get_text(strip=True)
    contest_start_time = contest_info[2].get_text(strip=True)
    contest_length = contest_info[3].get_text(strip=True)
    contest_register = contest_info[5].find("a")
    CODEFORCES_CLASS.CODEFORCES_CONTEST_REGISTER_URL = contest_register = CODEFORCES_URL + contest_register.get("href")
    output = f"**{contest_title}**\nStart time:   {contest_start_time}\nLength:   {contest_length}\nregister   {contest_register}\n"
    return output

##############################################################################
