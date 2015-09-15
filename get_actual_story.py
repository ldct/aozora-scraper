#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests
import os
import sys

def get_actual_story(url):
  r = requests.get(url)
  r.encoding = 'utf-8'

  soup = BeautifulSoup(r.text, 'lxml')

  download_table = soup.find_all('table', class_='download')

  assert len(download_table) == 1
  download_table = download_table[0]

  download_links = [l['href'] for l in download_table.find_all('a') if 'html' in l['href']]

  return download_links

for story_list_fn in os.listdir('stories'):
  full_fn = 'stories/' + story_list_fn
  with open(full_fn) as f:
    for story_url in f.readlines():
      truncated_story_url = story_url[:-1]
      print(truncated_story_url)
      print(get_actual_story(truncated_story_url))
      sys.stdout.flush()