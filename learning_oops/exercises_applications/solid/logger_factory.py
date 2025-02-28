from abc import ABC, abstractmethod


class Logger(ABC):
    @abstractmethod
    def log(self, message: str):
        pass


class ConsoleLogger(Logger):

    def __init__(self):
        self.type = 'console'

    def log(self, message: str):
        print('console logger started')


class FileLogger(Logger):
    def __init__(self, filename: str):
        self.filename = filename
        self.type = 'file'

    def log(self, message: str):
        with open(self.filename, 'a') as f:
            f.write(message)


class DatabaseLogger(Logger):
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.type = 'database'

    def log(self, message: str):
        print('database logger started')


class LoggingFactory:
    @staticmethod
    def create_logger(type: str, **kwargs) -> Logger:
        logging_class = {
            'console': ConsoleLogger,
            'file': FileLogger(filename=kwargs.get('filename')),
            'database': DatabaseLogger(db_name=kwargs['db_name'])
        }

        if type not in logging_class:
            raise NotImplementedError('Logging type must be one of the following: console, file, database')

        return logging_class[type]()


def main():
    logger = LoggingFactory.create_logger('console')
    logger.log('hello')



if __name__ == '__main__':
    main()
