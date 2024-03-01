from abc import ABC, abstractmethod

class Logger(ABC):
    @abstractmethod
    def log(self, message):
        pass

class LoggingLibrary(Logger):
    def log(self, message):
        # Implementation using a specific logging library like logging or loguru
        pass

class ConsoleLogger(Logger):
    def log(self, message):
        print(message)

class FileLogger(Logger):
    def __init__(self, file_path):
        self.file_path = file_path

    def log(self, message):
        with open(self.file_path, 'a') as file:
            file.write(message + '\n')

class LogManager:
    def __init__(self, logger: Logger):
        self.logger = logger

    def log_message(self, message):
        self.logger.log(message)

if __name__ == "__main__":
    # Example usage
    logging_library_logger = LoggingLibrary()
    console_logger = ConsoleLogger()
    file_logger = FileLogger('log.txt')

    # Injecting different loggers into the LogManager
    log_manager = LogManager(logging_library_logger)
    log_manager.log_message("This is a log message using the logging library")

    log_manager = LogManager(console_logger)
    log_manager.log_message("This is a log message printed to console")

    log_manager = LogManager(file_logger)
    log_manager.log_message("This is a log message written to file")
