#!/usr/bin/env python3

import os

for story_list_fn in os.listdir('stories'):
  full_fn = 'stories/' + story_list_fn
  with open(full_fn) as f:
    for story_url in f.readlines():
        print(story_url[:-1])