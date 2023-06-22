from linebot.models import *

keywords = [
    ["meow"],
    ["演講", "speech"],
    ['codeforces contest', 'cf', 'cf contest']
]

messages_items = []

for i in range(0, len(keywords)):
    tmp_message = QuickReplyButton(action=MessageAction(label=keywords[i][0], text=keywords[i][0]))
    messages_items.append(tmp_message)

QUICK_MESSAGE_BUTTON = QuickReply(messages_items)


auto_register_check = [
    QuickReplyButton(action=MessageAction(label='Yes', text='Yes')),
    QuickReplyButton(action=MessageAction(label='No', text='No'))
]

AUTO_RESIGTER_CHECK_BUTTON = QuickReply(auto_register_check)