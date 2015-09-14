#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests

ROOT_URL = 'http://www.aozora.gr.jp/'

def without_digits(s):
  return ''.join([i for i in s if not i.isdigit()])

def scrape_a_url(a_url):
  alpha = a_url.split('_')[-1].split('.')[0]
  alpha = without_digits(alpha)

  with open('stories_' + alpha, 'a+') as f:

    r = requests.get(a_url)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, 'lxml')

    main_table = soup.find_all('table', class_='list')

    assert len(main_table) == 1
    main_table = main_table[0]

    for link in main_table.find_all('a'):
      href = link['href']
      assert 'cards' in href
      href = href.split('../')[1]
      f.write(ROOT_URL + href + '\n')

    next_link = [link for link in soup.find_all('a') if link.text == '次の50件']

    if len(next_link) == 0: return

    assert len(next_link) == 2
    assert next_link[0]['href'] == next_link[1]['href']

    next_link_href = ROOT_URL + 'index_pages/' + next_link[0]['href']

    scrape_a_url(next_link_href)