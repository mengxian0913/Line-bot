# meow
from sent_messege import sentmessage
from User import *

def meow(token, user_id):
    sentmessage(token, "meow", user_id)
    return