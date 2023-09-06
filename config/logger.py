import logging


def setup_logger(name):
    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)  # You can set this to DEBUG, INFO, WARNING, etc.

    # Create console handler and set level to info
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)

    # Create formatter and add it to the handler
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)d - %(message)s"
    )
    handler.setFormatter(formatter)

    # Add handler to logger
    logger.addHandler(handler)

    return logger
