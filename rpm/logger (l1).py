import logging
from logging.handlers import RotatingFileHandler


class Logger:
    sngl = None

    def __new__(cls, *args, **kwargs):
        if cls.sngl is None:
            cls.sngl = super().__new__(cls, *args, **kwargs)
            cls.sngl._initialize()
        return cls.sngl

    def _initialize(self):

        self.logger = logging.getLogger('singleton_logger')
        self.logger.setLevel(logging.DEBUG)

        # обработчик, макс=5кбайи, 2 прошлых записей логов после ротации
        handler = RotatingFileHandler('res.log', maxBytes=5000, backupCount=2)
        handler.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(message)s  |   %(levelname)s   |   %(asctime)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def log(self, level, message):
        if level == 'debug':
            self.logger.debug(message)
        elif level == 'info':
            self.logger.info(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        elif level == 'critical':
            self.logger.critical(message)

        else:
            self.logger.info('Unknown log level: ' + message)


logger1 = Logger()
logger2 = Logger()

logger1.log('info', 'инф')
logger2.log('error', 'ошибка')

print(f'logger1 ID: {id(logger1)}')
print(f'logger2 ID: {id(logger2)}')
