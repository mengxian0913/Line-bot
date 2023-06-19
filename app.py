from config import line_bot_api, handler
import detect
from detect import (
    DETECT_NEWS,
    DETECT_START,
    CODEFORCES_CLASS
)

from auto_register_codeforces_contest import (
    REGISTER_CODEFORCES_CONTEST
)

from speech import getspeech
from meow import meow

from flask import (
    Flask,
    request, 
    abort
)
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
import threading
from copy import deepcopy
import requests
from bs4 import BeautifulSoup as bs


# Linebot setting

app = Flask(__name__)
friend_list = ["f22e1f29a5914bf5899bbff1f81431fb"]
group_list = []
reply_text = ""

DETECT = threading.Thread(target=DETECT_NEWS)

#######################################################

# All of the function
function_list = [meow, getspeech]

# linebot app

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
    global CODEFORCES_CLASS

    reply_token_copy = (event.reply_token)
    text = event.message.text.lower()

    if CODEFORCES_CLASS.ASK_STATE == 1:
        CODEFORCES_CLASS.ASK_STATE = 0
        if text == '1' or text == 'yes':
            print("go to register")
            crawler_thread = threading.Thread(target=REGISTER_CODEFORCES_CONTEST, args=(reply_token_copy,))
            crawler_thread.start()
            return
        
    now_event = 0
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




