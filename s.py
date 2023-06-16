import time
import requests
from bs4 import BeautifulSoup as bs
IECS_NEWS_URL = "https://www.iecs.fcu.edu.tw/news/"
FCU_URL = "https://www.iecs.fcu.edu.tw"

IECS_NEWS = ""
FIRST_SEARCH = 1

def Get_News():

    response = requests.get(IECS_NEWS_URL)
    soup = bs(response.text, "html.parser")
    post = soup.find(class_="post")

    post_title = post.find("a")
    post_title = post_title.get("href")
    # post_image = post.find_all("img")
    # post_image = FCU_URL + post_image[1].get("src")
    post_date = post.find("span", class_="day")
    post_month = post.find("span", class_="month")
    post_date = [post_date.text, post_month.text]
    post_link = IECS_NEWS_URL + post_title

    output = f"Title:   {post_title}\nLink:   {post_link}\nDate:   {post_date[1] + '/' + post_date[0]}\n"
    return output

while True:
    try:
        CURRENT_NEWS = Get_News()
        if IECS_NEWS != CURRENT_NEWS:
            IECS_NEWS = CURRENT_NEWS
            print(IECS_NEWS)
    except:
        break
    
    time.sleep(3600)