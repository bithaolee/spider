#!/usr/bin/env python
# encoding: utf-8

from googlesearch import search

keyword = '终南山'
for url in search(keyword, lang='en', pause=3):
    print(url)