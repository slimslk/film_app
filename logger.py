import logging


class Logger:
    __LOG_FILE = "./logs/server_error.log"

    def __init__(self, name, file_name):
        self.__logger = logging.getLogger(name)
        log_format = logging.Formatter("%(asctime)s | %(name)-13s | %(levelname)s: %(message)s", "%d-%m-%Y %H:%M:%S")
        log_console_handler = logging.StreamHandler()
        log_console_handler.setLevel(logging.INFO)
        log_console_handler.setFormatter(log_format)

        log_file_handler = logging.FileHandler(file_name)
        log_file_handler.setLevel(logging.ERROR)
        log_file_handler.setFormatter(log_format)

        self.__logger.addHandler(log_console_handler)
        self.__logger.addHandler(log_file_handler)
        self.__logger.setLevel(logging.INFO)

    @property
    def logger(self):
        return self.__logger
