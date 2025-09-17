from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(frozen=True)
class ErrorMessage:
    error: str
    detail: str


class ErrorHandler(ABC):
    def __init__(self):
        self.next_handler = None

    @abstractmethod
    def parse_error(self, message: ErrorMessage) -> None | str:
        pass

    def set_next_handler(self, next_handler):
        self.next_handler = next_handler
        return next_handler

    def handle_error(self, message: ErrorMessage):
        result = self.parse_error(message)
        if result is not None:
            return result
        if self.next_handler is not None:
            return self.next_handler.handle_error(message)

        return "unhandled error"


class RetryHandler(ErrorHandler):
    def parse_error(self, message: ErrorMessage) -> str | None:
        if message.error == "timeout":
            return "retried and resolved"
        return None


class LogHandler(ErrorHandler):
    def parse_error(self, message: ErrorMessage):
        if message.error == "warning":
            return "Logged warning"
        return None


class EscalateHandler(ErrorHandler):
    def parse_error(self, message: ErrorMessage):
        if message.error == "fatal":
            return "Escalated to support"
        return None


def main():
    # client code
    test_errors = [
        {"error": "timeout", "details": "Connection failed"},
        {"error": "warning", "details": "Low disk space"},
        {"error": "fatal", "details": "System crash"},
        {"error": "unknown", "details": "Weird issue"},
    ]
    r_handler = RetryHandler()
    e_handler = EscalateHandler()
    l_handler = LogHandler()

    r_handler.set_next_handler(e_handler).set_next_handler(l_handler)

    for error in test_errors:
        message = ErrorMessage(error=error["error"], detail=error["details"])
        result = r_handler.handle_error(message=message)
        print(result)


if __name__ == "__main__":
    main()
