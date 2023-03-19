import requests
import logger
import config
from retrying import retry

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
    except Exception as e:
        logger.logger.error("=== generate_reply_text ERROR! ===")
        logger.logger.error(e)
        reply = reply_on_error
        return reply

def is_over_message_length(message):
    # 140字以内でないとツイートできないので
    return len(message) > 140

@retry(
    stop_max_attempt_number=3,
    wait_fixed=500, # リトライ間隔
    retry_on_result=is_over_message_length
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
        json=payload
    ).json()

    logger.logger.info("=== send_chat response ===")
    logger.logger.info(response)

    message = response["choices"][0]["message"]["content"]
    return message

if __name__ == "__main__":
    text = ""
    print(generate_reply_text(text))