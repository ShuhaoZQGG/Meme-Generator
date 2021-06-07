from abc import ABC
from abc import abstractmethod
from typing import List
from .quote_model import QuoteModel


class IngestorInterface:

    allowed_extension = []

    @classmethod
    def can_ingest(cls,path):
        ext = path.split('.')[-1]
        return ext in cls.allowed_extension

    @classmethod
    @abstractmethod
    def parse(cls, path:str) -> List[QuoteModel]:
        pass

