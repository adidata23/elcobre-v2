import logging


class TestLogger:
    def __init__(self, log_file_name='test.log', log_level=logging.INFO):
        self.logger = logging.getLogger('TestLogger')
        self.logger.setLevel(log_level)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        file_handler = logging.FileHandler(log_file_name)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def exception(self, message):
        self.logger.exception(message)

    def critical(self, message):
        self.logger.critical(message)


if __name__ == '__main__':
    logger = TestLogger(log_file_name='test.log', log_level=logging.INFO)

    logger.info('This is an informational message.')
    logger.warning('This is a warning message.')
    logger.error('This is an error message.')
    try:
        1 / 0  # To generate an exception
    except Exception as e:
        logger.exception('An exception occurred:')
    logger.critical('This is a critical message.')
