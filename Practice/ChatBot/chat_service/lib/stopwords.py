"""
获取停用词
"""

from chat_service.config import config

stopwords = [i.strip() for i in open(config.stopwords_path,encoding="utf-8").readlines()]
