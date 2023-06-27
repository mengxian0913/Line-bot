#reply the current contest of codeforces
from detect import(
    CODEFORCES_CLASS
)
from linebot.models import *
from linebot import(
    LineBotApi
)
from config import *
from quick_message import AUTO_RESIGTER_CHECK_BUTTON
from User import *



def CODEFORCES_CURRENT_CONTEST(reply_token, user_id):
    CODEFORCES_CLASS.MESSAGE.quick_reply = Users[user_id].QUICK_MESSAGE_BUTTON
    line_bot_api.reply_message(
        reply_token,
        CODEFORCES_CLASS.MESSAGE
    )
    return