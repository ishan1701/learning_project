from text_formatter import TextFormatter, TextFormatterTypeMap, TitleTextFormatter, UpperTextFormatter, LowerTextFormatter
from enum import Enum

class TextFormatterStrategyFactory:
    @staticmethod
    def formatter(formatter_type: Enum) -> TextFormatter:
        if formatter_type == TextFormatterTypeMap.TITLE:
            return TitleTextFormatter()
        if formatter_type == TextFormatterTypeMap.UPPER:
            return UpperTextFormatter()
        if formatter_type == TextFormatterTypeMap.LOWER:
            return LowerTextFormatter()
        else:
            raise NotImplementedError(f'Type is not implemented: {formatter_type}')