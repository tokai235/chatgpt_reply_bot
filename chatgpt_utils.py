import os
import logger
import openai
import config

openai.api_key = config.openai_api_key

def generate_reply_text(reply_text):
    reply_text = "こんにちは"
    logger.logger.info("\n=== generate_reply_text reply_text ===")
    logger.logger.info(reply_text)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "関西弁で話して"},
            {"role": "system", "content": "発言の最後に「知らんけど。」をつけて"},
            {"role": "user", "content": reply_text},
        ],
    )
    logger.logger.info("\n=== generate_reply_text response ===")
    print(response.choices[0]["message"]["content"].strip())

    # text = "リプライありがとう！"
    # logger.logger.info(text)
    # return text