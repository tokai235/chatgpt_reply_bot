import tweepy
from dotenv import load_dotenv
load_dotenv()
from twitter_utils import *

twitter_client = tweepy.Client(
    config.bearer_token,
    config.consumer_key,
    config.consumer_secret,
    config.access_token,
    config.access_token_secret
)

def main():
    # rules = get_rules()
    # delete_all_rules(rules)
    # set_rules(config.account_id)
    # get_stream(twitter_client)
    generate_reply_text("")

if __name__ == "__main__":
    main()