## get luck
from User import Users
from config import (
    line_bot_api
)
from meow import meow

def LUCK_STATE(reply_token, user_id):
    if Users[user_id].horoscope_subscribe_state != 1:
        meow(reply_token, user_id)
        return
        
    Users[user_id].LUCK_MESSAGE.quick_reply = Users[user_id].QUICK_MESSAGE_BUTTON
    line_bot_api.reply_message(
        reply_token,
        Users[user_id].LUCK_MESSAGE
    )
    return