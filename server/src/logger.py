import logging
import sys
from pathlib import Path


def setup_logger():
    Path('server/logs').mkdir(parents=True, exist_ok=True)
    LOG_FORMAT = '[%(asctime)s] %(levelname)s [%(name)s:%(lineno)d] %(message)s'
    TIME_FORMAT = '%Y-%m-%d %H:%M:%S'
    logging.basicConfig(
        level=logging.INFO,
        format=LOG_FORMAT,
        datefmt=TIME_FORMAT,
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler('server/logs/app.log', encoding='utf-8'),
        ]
    )