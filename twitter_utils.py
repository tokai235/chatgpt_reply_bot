# ほぼこれ
# https://zenn.dev/ryo427/articles/aeb7aaf22aa8f9
import json
import os
import requests
import time
import traceback
from chatgpt_utils import generate_reply_text
from logger import Logger

bearer_token = os.environ['BEARER_TOKEN']
twitter_user_id = os.environ['TWITTER_USER_ID']
logger = Logger()

def bearer_oauth(r):
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2FilteredStreamPython"
    return r

def get_rules():
    response = requests.get(
        "https://api.twitter.com/2/tweets/search/stream/rules",
        auth=bearer_oauth
    )
    if response.status_code != 200:
        raise Exception(
            "Cannot get rules (HTTP {}): {}".format(response.status_code, response.text)
        )
    logger.log_info("\n=== get_rules response ===")
    logger.log_info(json.dumps(response.json()))
    return response.json()

def delete_all_rules(rules):
    if rules is None or "data" not in rules:
        return None

    ids = list(map(lambda rule: rule["id"], rules["data"]))
    payload = {"delete": {"ids": ids}}
    response = requests.post(
        "https://api.twitter.com/2/tweets/search/stream/rules",
        auth=bearer_oauth,
        json=payload
    )
    if response.status_code != 200:
        raise Exception(
            "Cannot delete rules (HTTP {}): {}".format(
                response.status_code, response.text
            )
        )
    logger.log_info("\n=== delete_all_rules response ===")
    logger.log_info(json.dumps(response.json()))

def set_rules(account_id):
    # このアカウントに対してのリプライを監視する
    rules = [
        {
            "value": f"@{account_id}" # アカウントに対するコメント
        },
        {
            "value": f"to:{account_id}" # ツイートに対するリプライ
        },
    ]
    payload = {"add": rules}
    response = requests.post(
        "https://api.twitter.com/2/tweets/search/stream/rules",
        auth=bearer_oauth,
        json=payload
    )
    if response.status_code != 201:
        raise Exception(
            "Cannot add rules (HTTP {}): {}".format(response.status_code, response.text)
        )
    logger.log_info("\n=== set_rules response ===")
    logger.log_info(json.dumps(response.json()))

def get_stream(twitter_client):
    stream_url = "https://api.twitter.com/2/tweets/search/stream"
    query = "?tweet.fields=in_reply_to_user_id,author_id"
    run = 1
    while run:
        try:
            with requests.get(
                stream_url + query,
                auth=bearer_oauth,
                stream=True
            ) as response:
                logger.log_info("\n=== get_stream response ===")
                logger.log_info(response.status_code)
                # エラーハンドリング
                if response.status_code != 200:
                    raise Exception(
                        "Cannot get stream (HTTP {}): {}".format(
                            response.status_code, response.text
                        )
                    )

                # ツイートの読み取り
                for response_line in response.iter_lines():
                    if not response_line:
                        continue

                    json_response = json.loads(response_line)
                    tweet_id = json_response["data"]["id"] # ツイートID
                    author_id = json_response["data"]["author_id"] # 投稿者のID
                    reply_text = json_response["data"]["text"] #相手の送ってきた内容

                    logger.log_info(json_response)

                    # 無限ループしないように自分への返信はしない
                    if author_id == twitter_user_id:
                        continue

                    # リプライを生成してtwitterにPOST
                    twitter_client.create_tweet(
                        text = generate_reply_text(reply_text),
                        in_reply_to_tweet_id = tweet_id
                    )

        except ChunkedEncodingError as chunkError:
            logger.log_info(traceback.format_exc())
            time.sleep(6)
            continue

        except ConnectionError as e:
            logger.log_info(traceback.format_exc())
            run += 1
            if run < 10:
                time.sleep(6)
                logger.log_info(f"再接続します {run}回目")
                continue
            else:
                run = 0
        except Exception as e:
            # some other error occurred.. stop the loop
            logger.log_info("Stopping loop because of un-handled error")
            logger.log_info(traceback.format_exc())
            run = 0

class ChunkedEncodingError(Exception):
    pass