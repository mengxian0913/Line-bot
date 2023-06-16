from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import time
import threading

# Linebot setting

app = Flask(__name__)
Channel_Secret = "75e8dc7494a50b1a0c7b5c59abaf799b"
Channel_AccessToken = "0vEVSYhpMI9ZY4Lp9JwaJ1x9FhnNn2jkTNypCXZlbQcK/8bMes5sWrLIjove5CnWKls8IxAitL7UhnsexrArSTKJUyEFeC7d4pF3FRPi04clSZ2uYsyw2+4ido5TxfWB0ZoHwSSNa3PkJFwrR7ByYwdB04t89/1O/w1cDnyilFU="
line_bot_api = LineBotApi(Channel_AccessToken)
handler = WebhookHandler(Channel_Secret)
friend_ids = line_bot_api.get_all_rich_menu_ids()

# nonfunction

def nonfunction():
    return "meow"


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

def getspeech():

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

    return reply_speech


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

IECS_NEWS = ""
def DETECT_NEWS():
    global IECS_NEWS
    while True:
        try:
            CURRENT_NEWS = Get_News()
            if IECS_NEWS != CURRENT_NEWS:
                IECS_NEWS = CURRENT_NEWS
                for friend_id in friend_ids:
                    line_bot_api.push_message(
                        friend_id,
                        TextSendMessage(text="@Vincent 資訊系新消息!!\n"+IECS_NEWS)
                    )
        except:
            break
            
        time.sleep(3600)

thread = threading.Thread(target=DETECT_NEWS)
thread.start()


# All of the function
function_list = [nonfunction, getspeech]

# linebot app

@app.route("/", methods=['GET'])
def home():
    return "Hello, World!"

@app.route("/callback", methods=['POST'])
def callback():
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
    for i in range(0, len(keywords)):
        for word in keywords[i]:
            if text == word:
             now_event = i
             break
        if now_event != 0:
            break

    
    reply_text = function_list[now_event]()
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply_text)
    )

if __name__ == "__main__":
    app.run()



