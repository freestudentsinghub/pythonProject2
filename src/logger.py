import logging


def setup_logger(name, log_file):
    logger = logging.getLogger(name)
    file_handler = logging.FileHandler(log_file)
    file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)
    logger.setLevel(logging.INFO)
    return logger