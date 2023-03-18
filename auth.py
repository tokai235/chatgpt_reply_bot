import os
from twitter import *
from dotenv import load_dotenv
load_dotenv()

app_name = os.environ['APP_NAME']
consumer_key = os.environ['CONSUMER_KEY']
consumer_secret = os.environ['CONSUMER_SECRET']

oauth_dance(
    app_name,
    consumer_key,
    consumer_secret,
    token_filename="./secret.txt",
    open_browser=False
)