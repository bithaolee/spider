#!/usr/bin/env python
# encoding: utf-8

import requests
from urlparse import urlparse
from urllib import unquote
from bs4 import BeautifulSoup
from util import get_random_user_agent

proxies = {
    'http': 'http://127.0.0.1:7890',
    'https': 'https://127.0.0.1:7890',
}
keyword = '终南山'

page = 1

def fetch_page(page):
    headers = {'user-agent': get_random_user_agent()}
    print(headers)
    url = 'https://www.google.com/search?q=%s&start=%s' % (keyword, (page - 1) * 10)
    r = requests.get(url, proxies=proxies, headers=headers)
    if r.status_code != 200:
        print('crawler page failed')
    data = parse_page(r.text)

def parse_page(html):
    data = []
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all('a')
    for item in items:
        url = item.get('href')
        if url and url.startswith('/url?q='):
            # row = {
            #     'domain': 
            # }
            url_object = urlparse(url.replace('/url?q=', ''))
            row = dict(
                domain=url_object.netloc,
                url=url
            )
            data.append(row)
    return data

if __name__ == "__main__":
    fetch_page(1)
    