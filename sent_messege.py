# SENT MESSEGE
from config import line_bot_api
from linebot.models import (
    MessageEvent,
    TextMessage, 
    TextSendMessage
)

def sentmessege(token, messege):
    line_bot_api.reply_message(
        token,
        TextSendMessage(text=messege)
    )
    return