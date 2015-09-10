#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests

ROOT_URL = 'http://www.aozora.gr.jp/'
r = requests.get(ROOT_URL)
r.encoding = 'utf-8'

soup = BeautifulSoup(r.text, 'lxml')
print(soup.prettify())