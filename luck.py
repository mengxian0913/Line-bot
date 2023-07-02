import time
from User import Users
from bs4 import BeautifulSoup as bs
import requests
from linebot.models import *
from datetime import datetime
from config import(
    line_bot_api
)


class destiny:
    def __init__(self, num, color, constellation, time) -> None:
        self.luckynumber = num
        self.luckycolor = color
        self.luckyconstellation = constellation
        self.luckytime = time

horoscope = destiny(None, None, None, None)

def get_the_horoscope(constellation):
    url = "https://astro.click108.com.tw/daily_10.php?iAstro=" +  str(constellation)
    response = requests.get(url)
    soup = bs(response.text, "html.parser")

    star_baby = soup.find('div', class_='STARBABY')
    star_baby = star_baby.find('img')
    star_baby = star_baby.get('src')

    today_word = soup.find('div', class_='TODAY_WORD')
    today_word = today_word.find('p')
    today_word = today_word.text

    lucky_number = soup.find('h4', class_='NUMERAL')
    lucky_number = lucky_number.text


    lucky_color = soup.find_all('div', class_='LUCKY')[1]
    lucky_color = lucky_color.find('h4')
    lucky_color = lucky_color.text
    

    luck_time = soup.find('h4', class_='TIME')
    luck_time = luck_time.text


    lucky_friend = soup.find_all('div', class_='LUCKY')[4]
    lucky_friend = lucky_friend.find('h4')
    lucky_friend = lucky_friend.text


    lucky_template = ButtonsTemplate(
        thumbnail_image_url = star_baby,
        title = "今日運勢",
        text = f"今日評語: {today_word}\n數字: {lucky_number}\n顏色: {lucky_color}\n貴人: {lucky_friend}",
        actions=[
            URIAction(
                label='查看更多',
                uri = url
            )
        ]
    )
            
    MESSAGE = TemplateSendMessage(
        alt_text = 'codeforces contest',
        template = lucky_template
    )

    return MESSAGE




def GET_LUCK():
    while True:
        try:
            current_time = datetime.now().time()
            if current_time.hour == 7 and current_time.minute == 40:
                for i in Users:
                    Users[i].LUCK_MESSAGE = get_the_horoscope(Users[i].constellation)
                    Users[i].push_LUCK_message()
        except:
            print("error")

        time.sleep(30)
