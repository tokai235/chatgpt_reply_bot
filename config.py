import os
from dotenv import load_dotenv
load_dotenv()
from file_utils import read_prompt

consumer_key = os.environ['CONSUMER_KEY']
consumer_secret = os.environ['CONSUMER_SECRET']
twitter_user_id = os.environ['TWITTER_USER_ID']
bearer_token = os.environ['BEARER_TOKEN']
access_token = os.environ['ACCESS_TOKEN']
access_token_secret = os.environ['ACCESSS_TOKEN_SECRET']
account_id = os.environ['ACCOUNT_ID']
app_name = os.environ['APP_NAME']

openai_api_key = os.environ["OPENAI_API_KEY"]
prompt = read_prompt('chatgpt_prompt.txt')
