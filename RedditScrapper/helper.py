from bs4 import BeautifulSoup
import requests
import time
import cv2
import numpy as np

def get_posts(headers:dict[str,str],subreddit:str):
    '''
    Gets posts from  "all time top posts" category and returns all the posts
    '''

    url = f"https://old.reddit.com/r/{subreddit}/top/?sort=top&t=all"
    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, "lxml")
    posts = soup.select(".thing")

    return posts

def get_comments_score_permalink(post):
    """
    Returns the number of comments, score(upvotes-downvotes) and the permalink of the reddit post
    """

    thing = post
    title = thing.select_one("a.title").get_text(strip=True)
    score = int(thing["data-score"])
    num_comments = int(thing["data-comments-count"])
    permalink = "https://old.reddit.com" + thing["data-permalink"]

    return (num_comments,score,permalink)

def get_body_text_image(permalink,headers:dict[str,str]):
    post_html = requests.get(permalink, headers=headers).text
    post_soup = BeautifulSoup(post_html, "lxml")
    expando = post_soup.select_one("div.expando")

    if expando:
        usertext = expando.select_one("div.usertext-body div.md")
        image_div = expando.select_one("div.media-preview-content")
        if not usertext:
            body_text = None
        else:
            body_text = usertext.get_text("\n",strip=True)
        
        image_url = None
        if image_div:
            link = image_div.select_one("a")
            if link and link.has_attr("href"):
                image_url = link["href"]
    
    return (body_text,image_url)