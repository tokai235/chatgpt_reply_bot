import logger
import openai
import config

openai.api_key = config.openai_api_key

def generate_reply_text(text):
    logger.logger.info("=== generate_reply_text text ===")
    logger.logger.info(text)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        timeout=10.0,
        messages=[
            {"role": "system", "content": config.prompt},
            {"role": "user", "content": text},
        ],
    )
    logger.logger.info("=== generate_reply_text response ===")
    logger.logger.info(response)

    reply = response.choices[0]["message"]["content"]
    return reply
