import requests
from bs4 import BeautifulSoup as bs
from linebot.models import *
from linebot import LineBotApi
from config import *
from quick_message import *
from User import *
# SPEECH NWES BOT
feng_chia_url = "https://www.iecs.fcu.edu.tw/"
url = "https://www.iecs.fcu.edu.tw/news/?category=speech"
dash = "------------------------------------------------"

columns = []


def catch(now, speech_title):

    #get image
    post_image = now.find('img', class_='img-fluid')
    post_image = post_image.get('src')
    post_image = feng_chia_url + post_image

    # getlink
    link = now.find(id="example")
    link = link.get("value")

    # get info
    main = now.find("table")
    text = main.get_text(strip=True)
    #print(text)

    # 解析演講資訊
    info = text.split("：")

    #print(info)

    date = info[1].split("演講時間")[0]
    time = info[2].split("演講者")[0]
    speaker = info[3].split("服務單位")[0]
    affiliation = info[4].split("演講題目")[0]
    topic = info[5].split("演講地點")[0]
    place = info[6].split("值日生")[0]

    speech_title = speech_title.split('】')[1]
    if len(speech_title) > 40:
        speech_title = speech_title[:30] + '...'

    speech = CarouselColumn(
            thumbnail_image_url = post_image,
            title = speech_title,
            text = 'Date: ' + date,
            actions=[
                URIAction(
                    label = '馬上查看',
                    uri = link
                )
            ]
    )

    columns.append(speech)

    return

def getspeech(reply_token_copy, user_id):
    global columns
    columns.clear()

    response = requests.get(url)
    soup = bs(response.text, "html.parser")

    post = soup.find_all(class_="post", limit=10)

    url_news = "https://www.iecs.fcu.edu.tw/news/"

    posts = []
    title = []

    for i in post:
        link = i.select_one(".post-image")
        link = link.select_one("a").get("href")
        title.append(link)
        link = url_news + link + "/"
        posts.append(link)

    for i in range(0, len(posts)):
        speech = requests.get(posts[i])
        soup2 = bs(speech.text, "html.parser")
        catch(soup2, title[i])


    template = CarouselTemplate(columns)
    carousel_template_message = TemplateSendMessage(
        alt_text= 'get speech',
        template= template,
        quick_reply= Users[user_id].QUICK_MESSAGE_BUTTON
    )

    line_bot_api.reply_message(
         reply_token_copy,
         carousel_template_message
    )

    return