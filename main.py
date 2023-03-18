import os
import tweepy
from dotenv import load_dotenv
load_dotenv()
from twitter_utils import *
import logging

consumer_key = os.environ['CONSUMER_KEY']
consumer_secret = os.environ['CONSUMER_SECRET']
access_token = os.environ['ACCESS_TOKEN']
access_token_secret = os.environ['ACCESSS_TOKEN_SECRET']
account_id = os.environ['ACCOUNT_ID']

twitter_client = tweepy.Client(bearer_token, consumer_key, consumer_secret, access_token, access_token_secret)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s:%(name)s - %(message)s",
    filename="chatgpt_reply_bot.log"
)

def main():
    rules = get_rules()
    delete_all_rules(rules)
    set_rules(account_id)
    get_stream(twitter_client)

if __name__ == "__main__":
    main()