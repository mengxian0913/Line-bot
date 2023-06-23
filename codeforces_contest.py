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



def CODEFORCES_CURRENT_CONTEST(token):
    
    line_bot_api.reply_message(
        token,
        CODEFORCES_CLASS.MESSAGE
    )
    return