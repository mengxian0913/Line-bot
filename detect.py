from setting import *
from quick_message import *
from config import line_bot_api, handler
from linebot import (
    LineBotApi,
    WebhookHandler
)
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
import time
from flask import (
    Flask,
    request, 
    abort
)
import requests
from bs4 import BeautifulSoup as bs
from quick_message import AUTO_RESIGTER_CHECK_BUTTON

##############################################################################


class CODEFORCES:
    def __init__(self, contest_title, contest_date, contest_duration, contest_register) -> None:
        self.CONTEST_TITLE = contest_title
        self.CONTEST_START_TIME = contest_date
        self.CONTEST_DURATION = contest_duration
        self.CONTEST_REGISTER_URL = contest_register
        self.IMG = 'https://cdn.iconscout.com/icon/free/png-256/free-code-forces-3628695-3029920.png'
        self.MESSAGE = None
        return


class IECS_NEWS:
    def __init__(self, title, link, date, img) -> None:
        self.TITLE = title
        self.LINK = link
        self.DATE = date
        self.IMG = img
        self.MESSAGE = None
        return

##############################################################################

CODEFORCES_CLASS = CODEFORCES(None, None, None, None)
IECS_NEWS_CLASS =  IECS_NEWS(None, None, None, None)

##############################################################################

# ALL NEWS ABOUT IECS

IECS_NEWS_URL = "https://www.iecs.fcu.edu.tw/news/"
FCU_URL = "https://www.iecs.fcu.edu.tw"
FIRST_SEARCH = 1

def GET_IECS_NEWS():

    response = requests.get(IECS_NEWS_URL)
    soup = bs(response.text, "html.parser")
    post = soup.find(class_="post")

    post_title = post.find("a")
    post_title = post_title.get("href")
    post_image = post.find_all("img")
    post_image = FCU_URL + post_image[1].get("src")
    post_date = post.find("span", class_="day")
    post_month = post.find("span", class_="month")
    post_date = post_month.text + '/' + post_date.text 
    post_link = IECS_NEWS_URL + post_title


    soup2 = requests.get(post_link)
    soup2 = bs(soup2.text, "html.parser")
    post_link = soup2.find('input', id='example')
    post_link = post_link.get('value')

    if len(post_title) >= 30:
        post_title = post_title[:30] + '...'

    IECS_NEWS_INFO = {
        'title': post_title,
        'image': post_image,
        'date': post_date,
        'link': post_link
    }

    #output = f"Title:   {post_title}\nLink:   {post_link}\nDate:   {post_date[1] + '/' + post_date[0]}\n"
    return IECS_NEWS_INFO

##############################################################################
# Codeforces contest

CODEFORCES_URL = "https://codeforces.com"
CODEFORCES_CONTEST_URL = "https://codeforces.com/contests"

def CODEFORCES_CONTEST():
    response = requests.get(CODEFORCES_CONTEST_URL)
    soup = bs(response.text, "html.parser")
    contest = soup.select_one("tr[data-contestid]")
    contest_info = contest.find_all("td")
    contest_title = contest_info[0].get_text(strip=True)
    contest_start_time = contest_info[2].get_text(strip=True)
    contest_length = contest_info[3].get_text(strip=True)
    contest_register = contest_info[5].find("a")
    contest_register = CODEFORCES_URL + contest_register.get("href")

    if len(contest_title) >= 30:
        contest_title = contest_title[:30] + '...'

    CODEFORCES_CONTEST_INFO = {
        'title': contest_title,
        'start_time': contest_start_time,
        'duration': contest_length,
        'register_link': contest_register
    }

    # output = f"{contest_title}\nStart time:   {contest_start_time}\nLength:   {contest_length}\nregister   {contest_register}\n" + "自動註冊請傳 1 或 Yes"
    return CODEFORCES_CONTEST_INFO

##############################################################################

## AUTO DETECT

def DETECT_NEWS():
    global Users
    global CODEFORCES_CLASS
    global IECS_NEWS_CLASS

    while True:
        try:
            IECS_CURRENT_NEWS = GET_IECS_NEWS()
            if IECS_NEWS_CLASS.TITLE != IECS_CURRENT_NEWS['title']:
                IECS_NEWS_CLASS.TITLE = IECS_CURRENT_NEWS['title']
                IECS_NEWS_CLASS.DATE = IECS_CURRENT_NEWS['date']
                IECS_NEWS_CLASS.LINK = IECS_CURRENT_NEWS['link']
                IECS_NEWS_CLASS.IMG = IECS_CURRENT_NEWS['image']

                iecs_template = ButtonsTemplate(
                    thumbnail_image_url= IECS_NEWS_CLASS.IMG,
                    title = IECS_NEWS_CLASS.TITLE,
                    text = f"Date: {IECS_NEWS_CLASS.DATE}",

                    actions=[
                        URIAction(
                            label = '點我查看更多',
                            uri = IECS_NEWS_CLASS.LINK
                         )
                    ]
                )

                IECS_NEWS_CLASS.MESSAGE = TemplateSendMessage(
                    alt_text='IECS news',
                    template=iecs_template,
                    quick_reply=QUICK_MESSAGE_BUTTON
                )
                
                for i in Users:
                    line_bot_api.push_message(
                        i,
                        IECS_NEWS_CLASS.MESSAGE
                    )


            CODEFORCES_CURRENT_NEWS = CODEFORCES_CONTEST()
            if CODEFORCES_CLASS.CONTEST_TITLE != CODEFORCES_CURRENT_NEWS['title']:
                
                for i in Users:
                    Users[i].codeforces_register_state = 1

                CODEFORCES_CLASS.CONTEST_TITLE = CODEFORCES_CURRENT_NEWS['title']
                CODEFORCES_CLASS.CONTEST_START_TIME = CODEFORCES_CURRENT_NEWS['start_time']
                CODEFORCES_CLASS.CONTEST_DURATION = CODEFORCES_CURRENT_NEWS['duration']
                CODEFORCES_CLASS.CONTEST_REGISTER_URL = CODEFORCES_CURRENT_NEWS['register_link']

                codeforces_template = ButtonsTemplate(
                    thumbnail_image_url = CODEFORCES_CLASS.IMG,
                    title = CODEFORCES_CLASS.CONTEST_TITLE,
                    text = f"Start: {CODEFORCES_CLASS.CONTEST_START_TIME}\nDuration: {CODEFORCES_CLASS.CONTEST_DURATION}",
                    actions=[
                        MessageAction(
                            label='Register',
                            text = 'Register'
                        )
                    ]
                )
                
                CODEFORCES_CLASS.MESSAGE = TemplateSendMessage(
                    alt_text = 'codeforces contest',
                    template = codeforces_template,
                    quick_reply = QUICK_MESSAGE_BUTTON
                )

                for i in Users:
                    line_bot_api.push_message(
                        i.user_id,
                        CODEFORCES_CLASS.MESSAGE
                    )

        except:
            break
            
        time.sleep(3600)
    return
