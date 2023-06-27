from bs4 import BeautifulSoup as bs
import requests


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
    

get_the_horoscope(1)    