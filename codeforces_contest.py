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
from meow import meow



def CODEFORCES_CURRENT_CONTEST(reply_token, user_id):
    if Users[user_id].codeforces_subscribe_state != 1:
        meow(reply_token, user_id)
        return

    CODEFORCES_CLASS.MESSAGE.quick_reply = Users[user_id].QUICK_MESSAGE_BUTTON
    Users[user_id].codeforces_register_state = 1
    line_bot_api.reply_message(
        reply_token,
        CODEFORCES_CLASS.MESSAGE
    )
    return