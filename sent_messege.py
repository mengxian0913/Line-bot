# SENT MESSEGE
from quick_message import *
from config import line_bot_api
from linebot.models import *
from User import *
from auto_register_codeforces_contest import(
    REGISTER_CODEFORCES_CONTEST
)
from detect import(
    CODEFORCES_CLASS
)
from linebot.models import *

def sentmessage(reply_token, messege, user_id):
    line_bot_api.reply_message(
        reply_token,
        TextSendMessage(text=messege, quick_reply=Users[user_id].QUICK_MESSAGE_BUTTON)
    )
    return