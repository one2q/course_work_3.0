import logging

logger_api = logging.getLogger("logger_api")

api_logger_handler = logging.FileHandler(filename="api.log", encoding="utf-8")

formatter_one = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")

api_logger_handler.setFormatter(formatter_one)

logger_api.addHandler(api_logger_handler)