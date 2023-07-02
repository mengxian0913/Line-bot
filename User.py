from config import(
    line_bot_api,
    IECS_NEWS_CLASS,
    CODEFORCES_CLASS,
    FCU_NEWS_CLASS
)
from quick_message import(
    codeforces_keywords,
    luck_keywords,
    keywords
)
from linebot.models import *

class User:

    def __init__(self, id, name, email, nid_account, nid_password, codeforces_handle, codeforces_password, constellation) -> None:
        self.user_id = id
        self.user_name = name
        self.email = email
        self.nid_account = nid_account
        self.nid_password = nid_password

        self.codeforces_handle = codeforces_handle
        self.codeforces_password = codeforces_password
        self.codeforces_register_state = 0

        self.constellation = constellation

        ## subscribe
        self.codeforces_subscribe_state = (len(self.codeforces_handle) != 0 and len(self.codeforces_password) != 0)
        self.horoscope_subscribe_state = (len(self.constellation) != 0)


        self.set_quick_message(self.codeforces_subscribe_state, self.horoscope_subscribe_state)
        self.push_all_message()

    def set_quick_message(self, codeforces_subscribe_state, horoscope_subscribe_state):
        global keywords
        self.KEYWORDS = keywords.copy()
        
        if codeforces_subscribe_state == 1:
            self.KEYWORDS.append(codeforces_keywords)

        if horoscope_subscribe_state == 1:
            self.KEYWORDS.append(luck_keywords)

        
        self.messages_items = []
        for i in range(0, len(self.KEYWORDS)):
            tmp_message = QuickReplyButton(action=MessageAction(label=self.KEYWORDS[i][0], text=self.KEYWORDS[i][0]))
            self.messages_items.append(tmp_message)
        
        self.QUICK_MESSAGE_BUTTON = QuickReply(self.messages_items)
        return

    def push_IECS_news(self):
        IECS_NEWS_CLASS.MESSAGE.quick_reply = self.QUICK_MESSAGE_BUTTON
        line_bot_api.push_message(
            self.user_id,
            IECS_NEWS_CLASS.MESSAGE
        )
        return

    def push_CODEFORCES_news(self):
        if self.codeforces_subscribe_state != 0:
            CODEFORCES_CLASS.MESSAGE.quick_reply = self.QUICK_MESSAGE_BUTTON
            line_bot_api.push_message(
                self.user_id,
                CODEFORCES_CLASS.MESSAGE
            )
            self.codeforces_register_state = 1
        return

    def push_FCU_news(self):
        FCU_NEWS_CLASS.MESSAGE.quick_reply = self.QUICK_MESSAGE_BUTTON
        line_bot_api.push_message(
            self.user_id,
            FCU_NEWS_CLASS.MESSAGE
        )
        return

    def push_all_message(self):
        self.push_FCU_news()
        self.push_IECS_news()   
        if self.codeforces_subscribe_state == 1:
            self.push_CODEFORCES_news()
        return
    
    def get_horoscope(self):
        return
    
            

Users = {}

# examlpe_user = User('example_id', 1, 1, 1, 1, 1, 1)
# Users['example_id'] = examlpe_user

# print(Users['example_id'].subscribe_codeforces_state)

# Users['example_id'].QUICK_MESSAGE_BUTTON