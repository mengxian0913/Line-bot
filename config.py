from linebot import (
    LineBotApi,
    WebhookHandler
)

Channel_Secret = "76945093850f04f157b85529561b4988"
Channel_AccessToken = "5p7Aj/8UlBFkhiwn0wgajxROjLJzh7ZHXZugP+wXe6fGCEAvLyiny45uV7z9kvqPVx/6jfEH4ToX0wYHYuTmz9WV51DfLTLvWkSL6NCyWFWTs8hDDfm28pR2MmjOEPh5kFxaQ1wBijIVSdPLqDBogwdB04t89/1O/w1cDnyilFU="
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
        self.URL = "https://codeforces.com/contests"
        return


class IECS_NEWS:
    def __init__(self, title, link, date, img) -> None:
        self.TITLE = title
        self.LINK = link
        self.DATE = date
        self.IMG = img
        self.MESSAGE = None
        return
    

class FCU_NEWS:
    def __init__(self, title, link, date, img) -> None:
        self.TITLE = title
        self.LINK = link
        self.DATE = date
        self.IMG = img
        self.MESSAGE = None

##############################################################################

CODEFORCES_CLASS = CODEFORCES(None, None, None, None)
IECS_NEWS_CLASS =  IECS_NEWS(None, None, None, None)
FCU_NEWS_CLASS = FCU_NEWS(None, None, None, None)

##############################################################################


##############################################################################
## form 
class form:
    url = ""

FORM = form()
##############################################################################
