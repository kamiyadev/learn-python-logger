# ==========================================================
# RotatingFileHandler / TimedRotatingFileHandler のサンプル
# ==========================================================
# このコードは「ログファイルを自動で分割（ローテーション）する方法」
# を学ぶためのサンプルです。
#
# 2種類のローテーション方法を使っています：
#
# 1. RotatingFileHandler
#    → ファイルサイズが一定を超えたら分割
#
# 2. TimedRotatingFileHandler
#    → 一定時間ごとに分割
# ==========================================================


import logging
import logging.handlers


# ----------------------------------------------------------
# ■ Logger（ログを出す人）を作成
# ----------------------------------------------------------
# "__name__" を渡すことで、
# このファイル名がロガー名になります。
logger = logging.getLogger(__name__)


# ----------------------------------------------------------
# ■ ① サイズで分割するハンドラー
# ----------------------------------------------------------
# RotatingFileHandler は
# ファイルサイズが maxBytes を超えたら
# 新しいファイルを作成します。
#
# maxBytes=1000
#   → 1000バイトを超えたら分割
#
# backupCount=5
#   → 古いログを最大5個まで保存
#      それ以上は自動削除されます。

r_handler = logging.handlers.RotatingFileHandler(
    "logs/rotating.log",   # 保存ファイル名
    maxBytes=1000,         # 最大サイズ（バイト）
    backupCount=5,         # 保存する世代数
    encoding="utf-8"       # 文字コード
)


# ----------------------------------------------------------
# ■ ② 時間で分割するハンドラー
# ----------------------------------------------------------
# TimedRotatingFileHandler は
# 一定時間ごとにファイルを分割します。
#
# when="s"
#   → 秒単位でローテーション
#
# interval=10
#   → 10秒ごとに分割
#
# backupCount=5
#   → 最大5世代保存

t_handler = logging.handlers.TimedRotatingFileHandler(
    "logs/timed_rotating.log",  # 保存ファイル名
    when="s",                   # 秒単位
    interval=10,                # 10秒ごと
    backupCount=5,              # 保存世代数
    encoding="utf-8"
)


# ----------------------------------------------------------
# ■ Loggerのレベル設定
# ----------------------------------------------------------
# DEBUG以上を処理対象にする
# DEBUG < INFO < WARNING < ERROR < CRITICAL
logger.setLevel(logging.DEBUG)


# ----------------------------------------------------------
# ■ Handlerのレベル設定
# ----------------------------------------------------------
# INFO以上のみファイルに出力されます
r_handler.setLevel(logging.INFO)
t_handler.setLevel(logging.INFO)


# ----------------------------------------------------------
# ■ ログの表示形式（Formatter）
# ----------------------------------------------------------
sample_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

# 各ハンドラーにフォーマッターを設定
r_handler.setFormatter(sample_formatter)
t_handler.setFormatter(sample_formatter)


# ----------------------------------------------------------
# ■ LoggerにHandlerを登録
# ----------------------------------------------------------
# これをしないとログは出力されません
logger.addHandler(r_handler)
logger.addHandler(t_handler)


# ----------------------------------------------------------
# ■ テスト用ログ出力
# ----------------------------------------------------------
# 1秒ごとにログを出します。
# 100回繰り返すので、
# サイズと時間の両方でローテーションが発生します。

import time

for _ in range(100):
    logger.debug("デバッグログ")      # 出力されない（HandlerがINFO以上）
    logger.info("infoログ")
    logger.warning("warningログ")
    logger.error("errorログ")
    logger.critical("criticalログ")

    time.sleep(1)