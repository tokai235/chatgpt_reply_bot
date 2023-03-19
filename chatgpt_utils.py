import logger
import openai
import config
from retrying import retry

openai.api_key = config.openai_api_key
reply_on_error = "ごめんやけど、うまく聞き取れへんかったわ。もう1回言ってくれるか？"

def generate_reply_text(text):
    logger.logger.info("=== generate_reply_text text ===")
    logger.logger.info(text)

    try:
        reply = send_chat(text)
        return reply
    except Exception as e:
        logger.logger.error(e)
        reply = reply_on_error
        return reply

def on_retry_error(e):
    logger.logger.error(e)
    return reply_on_error

@retry(
    stop_max_attempt_number=3,
    wait_fixed=500,
    retry_on_exception=on_retry_error
)
def send_chat(text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        timeout=5,
        messages=[
            {"role": "system", "content": config.prompt},
            {"role": "user", "content": text},
        ],
    )
    logger.logger.info("=== send_chat response ===")
    logger.logger.info(response)

    message = response.choices[0]["message"]["content"]
    return message
