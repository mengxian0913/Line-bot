# setting page
from config import(
    FORM,
    line_bot_api
)
from linebot.models import *
from User import Users

def USER_SETTING(reply_token, user_id):
    message = f"前往設定： {FORM.url}\n底下是你的 User ID(請小心保管!)\n"
    line_bot_api.reply_message(
        reply_token,
        TextSendMessage(text=message)
    )

    line_bot_api.push_message(
        user_id, 
        TextSendMessage(user_id, quick_reply=Users[user_id].QUICK_MESSAGE_BUTTON)
    )

    return