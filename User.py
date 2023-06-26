from config import(
    line_bot_api,
    IECS_NEWS_CLASS,
    CODEFORCES_CLASS
)

class User:
    def __init__(self, id, name, email, nid_account, nid_password, codeforces_handle, codeforces_password) -> None:
        self.user_id = id
        self.user_name = name
        self.email = email
        self.nid_account = nid_account
        self.nid_password = nid_password
        self.codeforces_handle = codeforces_handle
        self.codeforces_password = codeforces_password
        self.codeforces_register_state = 0
        self.codeforces_subscribe_state = (len(self.codeforces_handle) != 0 and len(self.codeforces_password) != 0)

    def push_all_message(self):
        line_bot_api.push_message(
            self.user_id,
            IECS_NEWS_CLASS.MESSAGE
        )

        if self.codeforces_subscribe_state == 1:
            line_bot_api.push_message(
                self.user_id,
                CODEFORCES_CLASS.MESSAGE
            )
            self.codeforces_subscribe_state = 1

    def push_IECS_news(self):
        line_bot_api.push_message(
            self.user_id,
            IECS_NEWS_CLASS.MESSAGE
        )

    def push_CODEFORCES_news(self):
        if self.codeforces_subscribe_state != 0:
            line_bot_api.push_message(
                self.user_id,
                CODEFORCES_CLASS.MESSAGE
            )
            self.codeforces_register_state = 1


Users = {}

# examlpe_user = User('example_id', 1, 1, 1, 1, 1, 1)
# Users['example_id'] = examlpe_user

# print(Users['example_id'].subscribe_codeforces_state)