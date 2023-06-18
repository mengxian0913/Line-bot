import time
import threading
import requests
from bs4 import BeautifulSoup as bs
CODEFORCES_URL = "https://codeforces.com"
CODEFORCES_CONTEST_URL = "https://codeforces.com/contests"
CODEFORCES_CONTEST_NEWS = ""

def CODEFORCES_CONTEST():

    response = requests.get(CODEFORCES_CONTEST_URL)
    soup = bs(response.text, "html.parser")
    contest = soup.select_one("tr[data-contestid]")
    contest_info = contest.find_all("td")
    contest_title = contest_info[0].get_text(strip=True)
    contest_start_time = contest_info[2].get_text(strip=True)
    contest_length = contest_info[3].get_text(strip=True)
    contest_register = contest_info[5].find("a")
    contest_register = CODEFORCES_URL + contest_register.get("href")
    output = f"**{contest_title}**\nStart time:   {contest_start_time}\nLength:   {contest_length}\nregister   {contest_register}\n"
    return output

def DETECT_NEWS():
    global CODEFORCES_CONTEST_NEWS
    while True:
        try:
            CURRENT_NEWS = CODEFORCES_CONTEST()
            if CODEFORCES_CONTEST_NEWS != CURRENT_NEWS:
                CODEFORCES_CONTEST_NEWS = CURRENT_NEWS
                print(CODEFORCES_CONTEST_NEWS)
        except:
            break
        
        time.sleep(5)


thread = threading.Thread(target=DETECT_NEWS)
thread.start()