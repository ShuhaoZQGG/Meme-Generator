from typing import List
from .quote_model import QuoteModel
from .CsvIngestor import CSVIngestor
from .DocxIngestor import DocxIngestor
from .PDFIngestor import PDFIngestor
from .TextIngestor import TextIngestor
from .ingestor_interface import IngestorInterface

class Ingestor(IngestorInterface):
    ingestors = [CSVIngestor,DocxIngestor,PDFIngestor,TextIngestor]

    @classmethod
    def parse(cls, path:str) -> List[QuoteModel]:
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)