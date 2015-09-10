#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests

ROOT_URL = 'http://www.aozora.gr.jp/'
r = requests.get(ROOT_URL)
r.encoding = 'utf-8'

soup = BeautifulSoup(r.text, 'lxml')
main_table = soup.find_all('table', summary='main')

assert len(main_table) == 1

tr = main_table[0].find_all('tr')[4]

alphabetical_links = tr.find_all('a')

for link in alphabetical_links:
  print(ROOT_URL + link['href'])