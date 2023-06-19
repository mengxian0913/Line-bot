from linebot import (
    LineBotApi,
    WebhookHandler
)

Channel_Secret = "8756120038fb41f4bc31560297cd1e9e"
Channel_AccessToken = "PU/J/S/o1mpxHkQS0fFJjwtutZGC6bZaoSZL7tsvNyzVdGMkJr+Ie4+uZeONsLO5nydcRcTKD0hALsBtdzOvnXqlRk/jBZclSiMyqZefDG2qtWa2utpPXXR7g1gab4eW9gQaAJ9x1A9s6naH+VO+9QdB04t89/1O/w1cDnyilFU="
line_bot_api = LineBotApi(Channel_AccessToken)
handler = WebhookHandler(Channel_Secret)
