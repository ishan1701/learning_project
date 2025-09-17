from text_formatter import TextFormatter


class Context:
    def __init__(self, formatter: TextFormatter):
        self._formatter = formatter

    # Here the formatter can be set during the runtime.
    # Hence, defining the getter and setter
    @property
    def formatter(self) -> TextFormatter:
        return self._formatter

    @formatter.setter
    def formatter(self, formatter: TextFormatter):
        self._formatter = formatter

    def run_formatter(self, text: str):
        return self.formatter.format(text=text)
