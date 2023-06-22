# SENT MESSEGE
from quick_message import *
from config import line_bot_api
from linebot.models import *
from auto_register_codeforces_contest import(
    REGISTER_CODEFORCES_CONTEST
)
from detect import(
    CODEFORCES_CLASS
)
from linebot.models import *


def sentmessege(token, messege):
    line_bot_api.reply_message(
        token,
        TextSendMessage(text=messege, quick_reply=QUICK_MESSAGE_BUTTON)
    )
    return