import logging
import re
from pathlib import Path

def setup_logger(log_file: str) -> logging.Logger:
    Path(log_file).parent.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger("women_safety")
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        handler = logging.FileHandler(log_file, encoding="utf-8")
        handler.setFormatter(logging.Formatter("%(asctime)s | %(levelname)s | %(message)s"))
        logger.addHandler(handler)
    return logger

def valid_phone(phone: str) -> bool:
    return bool(re.fullmatch(r"\+?[0-9][0-9\s-]{7,18}", phone.strip()))
