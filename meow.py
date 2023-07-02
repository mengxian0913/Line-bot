# meow
from linebot.models import *
from config import(
    line_bot_api
)
from User import Users

def meow(token, user_id):
    line_bot_api.reply_message(
        token,
        TextSendMessage(text="meow", quick_reply=Users[user_id].QUICK_MESSAGE_BUTTON)
    )
    return