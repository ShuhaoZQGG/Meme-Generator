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
        try:
            txt_file = open(path, 'r')
            for lines in txt_file.readlines():
                line = lines.strip('\n\r').strip()
                if(len(line) > 0):
                    parse = line.split('-')
                    new_quote = QuoteModel(str(parse[0].strip()),
                                           str(parse[1].strip()))
                    quotes.append(new_quote)
            txt_file.close()
        except Exception as e:
            raise Exception("txt parsing issue occured.")
        return quotes