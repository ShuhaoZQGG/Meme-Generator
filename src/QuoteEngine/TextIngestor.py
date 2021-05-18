from typing import List
from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel

class TextIngestor(IngestorInterface):
    allowed_extension = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception') 
        
        quotes = []
        with open(path, 'r') as infile:
            for line in infile:
                line = line.strip('\n')
                parse = line.split('-')
                new_quote =  QuoteModel(parse[0],parse[1])     
                quotes.append(new_quote)

        return quotes              