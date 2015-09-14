#!/usr/bin/env python3

from scrape_a_url import scrape_a_url

encountered_wo = False

with open('a_url') as f:
  for line in f.readlines():

    url = line[:-1]
    print(url)

    if 'nn1' in url:
      encountered_wo = True
      continue
    if not encountered_wo: continue

    scrape_a_url(url)