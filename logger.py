import logging
import logging.handlers


# ロガーの作成
log_formatter = "%(asctime)s - %(levelname)s:%(name)s - %(message)s"
logging.basicConfig(
    level=logging.INFO,
    format=log_formatter
)
logger = logging.getLogger(__name__)

# ログローテーションのハンドラーを設定
#   when: intervalの単位('S':秒、'M':分、'H':時間、'D':日、'W0'-'W6':曜日(0=月曜))
#   interval: ログローテーション間隔
#   backupCount: バックアップとして保持するログファイル数
handler = logging.handlers.TimedRotatingFileHandler(
    "bot.log", when="D", interval=1, backupCount=14
)
# フォーマットを設定
handler.setFormatter(logging.Formatter(log_formatter))
# ロガーにハンドラーを設定
logger.addHandler(handler)
