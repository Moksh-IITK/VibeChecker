from helper import get_posts
from helper import get_comments_score_permalink
from helper import get_body_text_image
import pandas as pd
import time

headers = {
    "User-Agent": "EngagementResearchBot/2.0 (academic)"
}

subreddit = "IITK"

posts = get_posts(headers,subreddit)

for post in posts[:2]:
    comments,score,permalink = get_comments_score_permalink(post)[0],get_comments_score_permalink(post)[1],get_comments_score_permalink(post)[2]
    time.sleep(5)
    body_text,image_url = get_body_text_image(permalink,headers)[0],get_body_text_image(permalink,headers)[1]
    print(comments,score)
    print(permalink)
    print("TEXT:")
    print(body_text)
    print("IMAGE URL:")
    print(image_url)
    print("-"*45)
