#reply the current contest of codeforces
from detect import(
    DETECT_CLASS,
)
from linebot.models import *
from linebot import(
    LineBotApi
)
from config import *
from quick_message import AUTO_RESIGTER_CHECK_BUTTON


def CODEFORCES_CURRENT_CONTEST(token):
    MESSEGE = DETECT_CLASS.CODEFORCES_CONTEST_NEWS
    flex_message = TextSendMessage(text=MESSEGE, quick_reply=AUTO_RESIGTER_CHECK_BUTTON)
    line_bot_api.reply_message(
        token,
        flex_message
    )
    return