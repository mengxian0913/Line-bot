from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, FollowEvent, JoinEvent
import time
import threading
from celery import Celery
from copy import deepcopy
output_lock = threading.Lock()

# Linebot setting

app = Flask(__name__)
Channel_Secret = "8756120038fb41f4bc31560297cd1e9e"
Channel_AccessToken = "PU/J/S/o1mpxHkQS0fFJjwtutZGC6bZaoSZL7tsvNyzVdGMkJr+Ie4+uZeONsLO5nydcRcTKD0hALsBtdzOvnXqlRk/jBZclSiMyqZefDG2qtWa2utpPXXR7g1gab4eW9gQaAJ9x1A9s6naH+VO+9QdB04t89/1O/w1cDnyilFU="

line_bot_api = LineBotApi(Channel_AccessToken)
handler = WebhookHandler(Channel_Secret)
friend_list = ["f22e1f29a5914bf5899bbff1f81431fb"]
group_list = []
reply_text = ""

##############################################################################

# nonfunction

def nonfunction(token):
    sentmessege(token, "meow")
    return

##############################################################################

# SPEECH NWES BOT

import requests
from bs4 import BeautifulSoup as bs
url = "https://www.iecs.fcu.edu.tw/news/?category=speech"
dash = "------------------------------------------------"

def catch(now):
        
    # getlink
            link = now.find(id="example")
            link = link.get("value")

        # get info
            main = now.find("table")
            text = main.get_text(strip=True)
        #print(text)

            # 解析演講資訊
            info = text.split("：")

        #print(info)

            date = info[1].split("演講時間")[0]
            time = info[2].split("演講者")[0]
            speaker = info[3].split("服務單位")[0]
            affiliation = info[4].split("演講題目")[0]
            topic = info[5].split("演講地點")[0]
            place = info[6].split("值日生")[0]

            # 格式化輸出
            ith_output = f"Link     : {link}\nDate     : {date}\nTime     : {time}\nSpeaker  : {speaker}\nAffiliation : {affiliation}\nTopic    : {topic}\nPlace    : {place}\n" + dash + "\n"
            return ith_output

def getspeech(reply_token_copy):

    response = requests.get(url)
    soup = bs(response.text, "html.parser")

    post = soup.find_all(class_="post", limit=10)

    url_news = "https://www.iecs.fcu.edu.tw/news/"

    posts = []
    title = []

    for i in post:
        link = i.select_one(".post-image")
        link = link.select_one("a").get("href")
        title.append(link)
        link = url_news + link + "/"
        posts.append(link)


    reply_speech = ""
    for i in range(0, len(posts)):
        reply_speech += title[i] + "\n"
        speech = requests.get(posts[i])
        soup2 = bs(speech.text, "html.parser")
        reply_speech += catch(soup2)
        
    sentmessege(reply_token_copy, reply_speech)
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

    response = requests.get(CODEFORCES_CONTEST_URL)
    soup = bs(response.text, "html.parser")
    contest = soup.select_one("tr[data-contestid]")
    contest_info = contest.find_all("td")
    contest_title = contest_info[0].get_text(strip=True)
    contest_start_time = contest_info[2].get_text(strip=True)
    contest_length = contest_info[3].get_text(strip=True)
    contest_register = contest_info[5].find("a")
    contest_register = CODEFORCES_URL + contest_register.get("href")
    output = f"**{contest_title}**\nStart time:   {contest_start_time}\nLength:   {contest_length}\nregister   {contest_register}\n"
    return output

##############################################################################

IECS_NEWS = ""
CODEFORCES_CONTEST_NEWS = ""
DETECT_START = 0

def DETECT_NEWS():
    global IECS_NEWS
    global CODEFORCES_CONTEST_NEWS

    while True:
        try:
            CURRENT_NEWS = Get_News()
            print(CURRENT_NEWS)
            if IECS_NEWS != CURRENT_NEWS:
                IECS_NEWS = CURRENT_NEWS
                line_bot_api.broadcast(
                    TextSendMessage(text="@Vincent 資訊系新消息!!\n"+IECS_NEWS)
                )

            CURRENT_NEWS = CODEFORCES_CONTEST()
            print(CURRENT_NEWS)
            if CODEFORCES_CONTEST_NEWS != CURRENT_NEWS:
                CODEFORCES_CONTEST_NEWS = CURRENT_NEWS
                line_bot_api.broadcast(
                    TextSendMessage(text="@Vincent Codeforces!!\n"+CODEFORCES_CONTEST_NEWS)
                )

        except:
            break
            
        time.sleep(3600)
    return

DETECT = threading.Thread(target=DETECT_NEWS)
#######################################################

# All of the function
function_list = [nonfunction, getspeech]

# linebot app

def sentmessege(token, messege):
    line_bot_api.reply_message(
        token,
        TextSendMessage(text=messege)
    )
    return

@app.route("/", methods=['GET'])
def home():
    return "Hello, World!"


@app.route("/callback", methods=['POST'])
def callback():
    global DETECT_START

    if DETECT_START == 0:
        DETECT.start()
        DETECT_START = 1

    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


keywords = [["."], ["演講", "speech"]]
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text.lower()
    now_event = 0
    reply_token_copy = (event.reply_token)

    for i in range(0, len(keywords)):
        for word in keywords[i]:
            if text == word:
             now_event = i
             break
        if now_event != 0:
            break

    crawler_thread = threading.Thread(target=function_list[now_event], args=(reply_token_copy,))
    crawler_thread.start()

    return

if __name__ == "__main__":
    app.debug = True
    app.run(port=5001)




