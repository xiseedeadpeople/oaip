from bs4 import BeautifulSoup  # pip install requests lxml bs4
import requests
from urllib.request import urlopen
import re as r

# 1.        headers                (V)      >>>     https://stackoverflow.com/questions/38489386
# 2.        <Response [200]>       (V)      >>>     https://stackoverflow.com/questions/43354200
# 3.        ???????                (?)


# func to get ip
def get_ip():
    try:
        d = str(urlopen('http://checkip.dyndns.com/').read())
        return r.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(d).group(1)

    except Exception as e:
        return e


# func to get headers
def asd():  # >>> 'python-requests/2.32.3'
    url = 'https://www.whatismybrowser.com/detect/what-is-my-user-agent/'

    try:
        response = requests.get(url).text
        soup = BeautifulSoup(response, 'lxml')
        nouns = soup.find(class_='detected_result technical-lookin')
        print(nouns.text)

    except Exception as e:
        print(e)


# func to check ip on ip-api
def ip_api_check(addr: str):
    url = f'https://ip-api.com/#{addr}'

    # headers = ... try 'https://httpbin.org/headers' - User-Agent
    # https://www.zenrows.com/blog/python-requests-user-agent#set-user-agent
    #

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
               'AppleWebKit/537.36 (KHTML, like Gecko) '
               'Chrome/130.0.0.0 Safari/537.36'}
    try:
        responce = requests.get(url, headers=headers)
        print(responce.text)

    except Exception as e:
        print(e)


# print(get_ip())       >>>         213.87.96.9
# ip_api_check(get_ip())

ip_api_check('213.87.96.9')
pass
