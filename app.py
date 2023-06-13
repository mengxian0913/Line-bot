from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)
Channel_Secret = "75e8dc7494a50b1a0c7b5c59abaf799b"
Channel_AcessToken = "0vEVSYhpMI9ZY4Lp9JwaJ1x9FhnNn2jkTNypCXZlbQcK/8bMes5sWrLIjove5CnWKls8IxAitL7UhnsexrArSTKJUyEFeC7d4pF3FRPi04clSZ2uYsyw2+4ido5TxfWB0ZoHwSSNa3PkJFwrR7ByYwdB04t89/1O/w1cDnyilFU="
line_bot_api = LineBotApi(Channel_AcessToken)
handler = WebhookHandler(Channel_Secret)

@app.route("/", methods=['GET'])
def home():
    return "Hello, World!"

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text
    line_bot_api.send_seen(event.source.user_id)
    reply_text = 'Hello, ' + text
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply_text)
    )

if __name__ == "__main__":
    app.run()
