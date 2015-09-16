# aozora-scraper
aozora-scraper


```
./scrape_root.py > ./a_url
./scrape_all_a_url.py
mv stories_* stories/
./get_actual_story.py > ./stories_links_logs
cat ./stories_links_logs | wc -l
./print_stories.py | wc -l
./find_outlier_stories.py > outliers.log
./find_hosted_stories.py > hosted_stories
```