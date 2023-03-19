import requests
import logger
import config
from retrying import retry
import retrying
from text_utils import truncated_text

reply_on_error = "ごめんやけど、うまく聞き取れへんかったわ。もう1回言ってくれるか？"

def bearer_oauth(r):
    r.headers["Authorization"] = f"Bearer {config.openai_api_key}"
    r.headers["Content-Type"] = "application/json"
    return r

def generate_reply_text(text):
    logger.logger.info("=== generate_reply_text text ===")
    logger.logger.info(text)

    try:
        reply = send_chat(text)
        return reply
    except retrying.RetryError as e:
        logger.logger.error("=== generate_reply_text RetryError! ===")
        logger.logger.error(e)
        reply = reply_on_error
        return reply
    except Exception as e:
        logger.logger.error("=== generate_reply_text Error! ===")
        logger.logger.error(e)
        reply = reply_on_error
        return reply

@retry(
    stop_max_attempt_number=3,
    wait_fixed=500, # リトライ間隔
    wrap_exception=True,
)
def send_chat(text):
    logger.logger.info("=== send_chat request ===")
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": config.prompt},
            {"role": "user", "content": text},
        ],
    }
    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        auth=bearer_oauth,
        json=payload,
        timeout=10,
    ).json()

    logger.logger.info("=== send_chat response ===")
    logger.logger.info(response)

    message = response["choices"][0]["message"]["content"]
    # ツイッターは140字までしかツイートできないので切り詰める
    return truncated_text(message)

if __name__ == "__main__":
    text = ""
    logger.logger.info(generate_reply_text(text))