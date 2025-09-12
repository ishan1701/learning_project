from abc import ABC, abstractmethod
from enum import Enum


class TextFormatter(ABC):
    @abstractmethod
    def format(self, text: str) -> str:
        pass


class UpperTextFormatter(TextFormatter):
    def format(self, text: str) -> str:
        return text.upper()


class LowerTextFormatter(TextFormatter):
    def format(self, text: str) -> str:
        return text.lower()


class TitleTextFormatter(TextFormatter):
    def format(self, text: str) -> str:
        return text.title()


class TextFormatterTypeMap(Enum):
    TITLE = TitleTextFormatter
    UPPER = UpperTextFormatter
    LOWER = LowerTextFormatter
