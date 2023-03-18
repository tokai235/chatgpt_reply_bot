# 別アカウントの access_token 取得用
# $ python auth.py
from twitter import *
import config

oauth_dance(
    config.app_name,
    config.consumer_key,
    config.consumer_secret,
    token_filename="./secret.txt",
    open_browser=False
)