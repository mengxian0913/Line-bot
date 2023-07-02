import threading
from config import (
    line_bot_api, 
    handler, 
    FORM
)
from User import *
from codeforces_contest import *
from auto_register_codeforces_contest import *
from speech import *
from meow import *
from quick_message import *
from user_setting_page import(
    USER_SETTING
)

from detect import (
    CODEFORCES_CLASS,
    IECS_NEWS_CLASS,
    DETECT_NEWS
)


from flask import (
    Flask,
    request, 
    abort,
    render_template,
    url_for
)
from linebot import (
    LineBotApi,
    WebhookHandler
)
from linebot.exceptions import InvalidSignatureError
from linebot.models import (
    MessageEvent,
    TextMessage, 
    TextSendMessage,
    FollowEvent,
    events
)


############################################################

# Linebot setting

app = Flask(__name__)
friend_list = ["f22e1f29a5914bf5899bbff1f81431fb"]
group_list = []
reply_text = ""

DETECT = threading.Thread(target=DETECT_NEWS)
DETECT_START = 0
#######################################################

# All of the function
# function_list = [meow, getspeech, CODEFORCES_CURRENT_CONTEST]

function_dic = {
    'meow': meow,
    '演講': getspeech,
    '設定': USER_SETTING,
    'codeforces contest': CODEFORCES_CURRENT_CONTEST
}

# linebot app
#######################################################

@app.route("/", methods=['GET'])
def home():
    return "Hello, World!"


@app.route("/callback", methods=['POST'])
def callback():
    global DETECT_START
    if DETECT_START == 0:
        DETECT.start()
        DETECT_START = 1

    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    global CODEFORCES_CLASS, FORM
    reply_token_copy = (event.reply_token)
    text = event.message.text.lower()
    current_user_id = event.source.user_id

    if Users.get(current_user_id) == None:
        FORM.url = request.host_url + 'form'
        messege = f"請填寫個人信息啟動 meowmeow bot!:    {FORM.url}"
        line_bot_api.reply_message(
            reply_token_copy,
            TextSendMessage(text = messege + "\n 底下是你的 user id! \n(p.s.請小心保管你的個資!!)")
        )
        
        line_bot_api.push_message(current_user_id, TextSendMessage(text=current_user_id))
        return

    if Users[current_user_id].codeforces_register_state == 1:
        if text == 'register':
            print("go to register")
            crawler_thread = threading.Thread(target=REGISTER_CODEFORCES_CONTEST, args=(reply_token_copy, Users[current_user_id].codeforces_handle, Users[current_user_id].codeforces_password, current_user_id, ))
            crawler_thread.start()
            return
        

    now_event = None
    try:
        now_event = function_dic[text]
    except:
        now_event = meow

    crawler_thread = threading.Thread(target=now_event, args=(reply_token_copy, current_user_id, ))
    crawler_thread.start()

    return



@handler.add(event=events.FollowEvent)
def handle_follow(event):
    print("new member join")
    FORM.url = request.host_url + 'form'
    user_id = event.source.user_id
    message = "歡迎加入Meowmeow Line Bot！請填寫表單提供信息完成設定！"
    line_bot_api.push_message(user_id, TextSendMessage(text=message + "\n" + FORM.url + "\n 底下是你的 user id! \n(p.s.請小心保管你的個資!!)"))
    line_bot_api.push_message(user_id, TextSendMessage(text=user_id))
    return "please setting the required information to start the function!"


@app.route('/form', methods=['GET', 'POST'])
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    print("Success to submit the form!")

    user_id = request.form.get('user_id')
    name = request.form.get('username')
    email = request.form.get('email')
    nid_account = request.form.get('NID_Account')
    nid_password = request.form.get('NID_Password')
    codeforces_handle = request.form.get('Codeforces_Handle')
    codeforces_password = request.form.get('Codeforces_Password')
    constellation = request.form.get('constellation')
    
    line_bot_api.push_message(
        user_id,
        TextSendMessage(text="恭喜你成功啟動 MEOW MEOW BOT !!")
    )

    Users[user_id] = (User(user_id, name, email, nid_account, nid_password, codeforces_handle, codeforces_password, constellation))

    return "表單提交成功！"

if __name__ == "__main__":
    app.debug = True
    app.run(port=5001)