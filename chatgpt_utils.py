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
        logger.logger.error("=== generate_reply_text ERROR! ===")
        logger.logger.error(e)
        reply = reply_on_error
        return reply

@retry(
    stop_max_attempt_number=3,
    wait_fixed=500, # リトライ間隔
)
def send_chat(text):
    logger.logger.info("=== send_chat request ===")
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
