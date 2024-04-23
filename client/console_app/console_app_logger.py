import logging


class Logger:
    __LOG_FILE = "./logs/console_app_error.log"
    __LOG_FORMAT = logging.Formatter("%(asctime)s | %(name)-13s | %(levelname)s: %(message)s", "%d-%m-%Y %H:%M:%S")

    __log_console_handler = logging.StreamHandler()
    __log_console_handler.setLevel(logging.WARNING)
    __log_console_handler.setFormatter(__LOG_FORMAT)

    __log_file_handler = logging.FileHandler(__LOG_FILE)
    __log_file_handler.setLevel(logging.ERROR)
    __log_file_handler.setFormatter(__LOG_FORMAT)

    logging.getLogger("").addHandler(__log_console_handler)
    logging.getLogger("").addHandler(__log_file_handler)

    def __init__(self, class_name):
        self.__logger = logging.getLogger(class_name)
        self.__logger.setLevel(logging.INFO)

    @property
    def logger(self):
        return self.__logger
