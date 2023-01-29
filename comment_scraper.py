import requests
import pandas as pd
import numpy as np
import praw
import csv

with open('passwords/client_id.txt', 'r') as f:
    CLIENT_ID = f.read()

with open('passwords/secret_key.txt', 'r') as f:
    SECRET_KEY = f.read()

# auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEY)

# This is my password please don't share ahhahah
# Place this comment_scraper.py file in the same directory as your csv file
with open('passwords/pw.txt', 'r') as f:
    pw = f.read()

reddit = praw.Reddit(client_id=CLIENT_ID, client_secret=SECRET_KEY, user_agent="glowguide")


# Replace with the links for your posts
# posts = [
#     "https://www.reddit.com/r/beauty/comments/y06c7x/what_are_your_thoughts_on_the_clinique_black/",
#     "https://www.reddit.com/r/Makeup/comments/tkaktc/is_clinique_black_honey_worth_it/",
#     "https://www.reddit.com/r/PaleMUA/comments/pc5mjl/clinique_black_honey_almost_lipstick_the_queen_of/",
#     "https://www.reddit.com/r/Makeup/comments/z7cbfl/opinion_on_cliniques_black_honey/",
#     "https://www.reddit.com/r/MakeupAddiction/comments/yxx6sr/is_the_clinique_almost_lipstick_in_black_honey/",
#     "https://www.reddit.com/r/Sephora/comments/tv7r1b/clinique_black_honey_not_what_i_was_expecting_the/"
# ]

posts = [
    "https://www.reddit.com/r/AsianBeauty/comments/m3zqir/reviewswatches_of_my_favorite_romand_juicy_and/",
    "https://www.reddit.com/r/AsianBeauty/comments/ivg0gk/12_facelip_swatches_mini_review_of_romand_juicy/",
    "https://www.reddit.com/r/AsianBeauty/comments/n2m4g2/reviewswatches_new_romand_juicy_lasting_tint/",
    "https://www.reddit.com/r/AsianBeauty/comments/y8lrpb/my_romand_juicy_lasting_tint_collection/",
    "https://www.reddit.com/r/AsianBeauty/comments/tvpnnp/romand_juicy_lasting_tint_bare_juicy/",
    "https://www.reddit.com/r/AsianBeauty/comments/isdyv6/romandromnd_juicy_lasting_tint_review_face/"
]

# Iterate through the different posts
for post in posts:
    print(post)
    submission = reddit.submission(url=post)
    # create a file with the name you'll provide as the file path
    with open("romand_juicy.csv", "a") as csvfile:
        comment_writer = csv.writer(csvfile)
        for comment in submission.comments:
            comment_writer.writerow([comment.body])