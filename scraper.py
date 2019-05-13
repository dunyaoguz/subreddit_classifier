import requests
import json
import pandas as pd
import re
from time import sleep

def fetch_page(subreddit, after=''):
    URL = f'https://www.reddit.com/r/{subreddit}.json'
    headers = {'User-agent': 'webscraping bot'}
    params = {'after': after}
    r = requests.get(URL, headers=headers, params=params)
    return r.json()['data']['children']

def parse_post(post):
    keep = ['subreddit', 'selftext', 'title', 'score', 'num_comments', 'author', 'permalink', 'stickied', 'url', 'name']
    data = post['data']
    return {k: v for k, v in data.items() if k in keep}

def parse_page(page):
    parsed_posts = []
    after = ''
    for post in page:
        p = parse_post(post)
        after = p['name']
        parsed_posts.append(p)
    return parsed_posts, after

def fetch_subreddit(subreddit, pages=4):
    all_posts = []
    after = ''
    for i in range(pages):
        print(f'Fetching Page {i + 1}')
        page = fetch_page(subreddit, after)
        parsed_posts, after = parse_page(page)
        all_posts.extend(parsed_posts)
        sleep(5)
    return all_posts

all_posts = fetch_subreddit('showerthoughts', pages=40)
shower_thoughts = pd.DataFrame(all_posts)

all_posts_2 = fetch_subreddit('crazyideas', pages=40)
crazy_ideas = pd.DataFrame(all_posts_2)

# crazy_ideas.to_csv('data/crazy_ideas.csv', index=False)
# shower_thoughts.to_csv('data/shower_thoughts.csv', index=False)
crazy_ideas.to_csv('data/crazy_ideas_2.csv', index=False)
shower_thoughts.to_csv('data/shower_thoughts_2.csv', index=False)
