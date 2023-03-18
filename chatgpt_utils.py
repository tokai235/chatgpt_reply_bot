import logging
from logger import Logger

logger = Logger()

def generate_reply_text(reply_text):
    logger.log_info("\n=== generate_reply_text reply_text ===")
    logger.log_info(reply_text)
    text = "リプライありがとう！"
    logger.log_info(text)
    return text