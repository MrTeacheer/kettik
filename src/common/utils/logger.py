import logging


class ColorizedHandler(logging.StreamHandler):
    COLORS = {
        "INFO": "\033[94m",  # Синий для INFO
        "WARNING": "\033[93m",  # Желтый для WARNING
        "ERROR": "\033[91m",  # Красный для ERROR
        "CRITICAL": "\033[41m",  # Красный фон для CRITICAL
        "DEBUG": "\033[92m",  # Зеленый для DEBUG
        "RESET": "\033[0m",  # Сброс цвета
    }

    def emit(self, record):
        log_message = self.format(record)
        color = self.COLORS.get(record.levelname, self.COLORS["RESET"])
        self.stream.write(color + log_message + self.COLORS["RESET"] + "\n")
        self.flush()


def setup_logger():
    logger = logging.getLogger("colored_logger")
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    colorized_handler = ColorizedHandler()
    colorized_handler.setFormatter(formatter)

    logger.addHandler(colorized_handler)

    return logger


logger = setup_logger()
