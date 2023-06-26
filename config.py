from linebot import (
    LineBotApi,
    WebhookHandler
)

Channel_Secret = "8756120038fb41f4bc31560297cd1e9e"
Channel_AccessToken = "PU/J/S/o1mpxHkQS0fFJjwtutZGC6bZaoSZL7tsvNyzVdGMkJr+Ie4+uZeONsLO5nydcRcTKD0hALsBtdzOvnXqlRk/jBZclSiMyqZefDG2qtWa2utpPXXR7g1gab4eW9gQaAJ9x1A9s6naH+VO+9QdB04t89/1O/w1cDnyilFU="
line_bot_api = LineBotApi(Channel_AccessToken)
handler = WebhookHandler(Channel_Secret)

##############################################################################
## NEWS

class CODEFORCES:
    def __init__(self, contest_title, contest_date, contest_duration, contest_register) -> None:
        self.CONTEST_TITLE = contest_title
        self.CONTEST_START_TIME = contest_date
        self.CONTEST_DURATION = contest_duration
        self.CONTEST_REGISTER_URL = contest_register
        self.IMG = 'https://cdn.iconscout.com/icon/free/png-256/free-code-forces-3628695-3029920.png'
        self.MESSAGE = None
        return


class IECS_NEWS:
    def __init__(self, title, link, date, img) -> None:
        self.TITLE = title
        self.LINK = link
        self.DATE = date
        self.IMG = img
        self.MESSAGE = None
        return

##############################################################################

CODEFORCES_CLASS = CODEFORCES(None, None, None, None)
IECS_NEWS_CLASS =  IECS_NEWS(None, None, None, None)

##############################################################################