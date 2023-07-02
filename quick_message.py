from linebot.models import *

codeforces_keywords = ['codeforces contest', 'cf', 'cf contest']
luck_keywords = ['運勢', 'luck']

keywords = [
    ["meow"],
    ["演講", "speech"],
    ['設定', 'setting']
]

###################################################################################################

auto_register_check = [
    QuickReplyButton(action=MessageAction(label='Yes', text='Yes')),
    QuickReplyButton(action=MessageAction(label='No', text='No'))
]

AUTO_RESIGTER_CHECK_BUTTON = QuickReply(auto_register_check)





# messages_items = []

# for i in range(0, len(keywords)):
#     tmp_message = QuickReplyButton(action=MessageAction(label=keywords[i][0], text=keywords[i][0]))
#     messages_items.append(tmp_message)

# QUICK_MESSAGE_BUTTON = QuickReply(messages_items)