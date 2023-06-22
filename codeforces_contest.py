#reply the current contest of codeforces
from detect import(
    DETECT_CLASS,
    auto_register_check,
    CODEFORCES_CLASS
)
from linebot.models import *
from linebot import(
    LineBotApi
)
from config import *



def CODEFORCES_CURRENT_CONTEST(token):
    global CODEFORCES_CLASS
    CODEFORCES_CLASS.ASK_STATE = 1
    MESSEGE = DETECT_CLASS.CODEFORCES_CONTEST_NEWS
    flex_message = TextSendMessage(text=MESSEGE, quick_reply=QuickReply(auto_register_check))
    line_bot_api.reply_message(
        token,
        flex_message
    )
    return