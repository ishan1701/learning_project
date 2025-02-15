from abc import ABC, abstractmethod
from pathlib import Path
from fpdf import FPDF


class BillReport:
    def __init__(self, file_name: str, file_path: str):
        self.file_name = file_name
        self.file_path = file_path

    @abstractmethod
    def generate(self, data):
        pass


class PdfReport(BillReport):
    def __init__(self, file_name: str, file_path: str, file_type: str):
        self.file_type = 'pdf'
        super().__init__(file_name=file_name, file_path=file_path)

    def generate(self, data):
        pass


class CSVReport(BillReport):
    def __init__(self, file_name: str, file_path: str, file_type: str):
        self.file_type = 'csv'
        super().__init__(file_name=file_name, file_path=file_path)

    def generate(self, data):
        pass


def generate_report(file_name: str, file_path: str, file_type: str):
    report_classes = {
        'pdf': PdfReport,
        'csv': CSVReport
    }

    if file_type.lower() in report_classes:
        return report_classes[file_type.lower()](file_name=file_name, file_path=file_path, file_type=file_type)

    raise NotImplementedError(f'{file_type} is not implemented.')
