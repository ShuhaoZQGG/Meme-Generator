import os
import random
import argparse
import MemeEngine
# @TODO Import your Ingestor and MemeEngine classes
from QuoteEngine import Ingestor, quote_model
from QuoteEngine.ingestor import Ingestor
from MemeEngine import Meme_Generator
from MemeEngine.Meme_Generator import Meme_Generator

def generate_meme(path=None, body=None, author=None):
    """ Generate a meme given an path and a quote """
 
    if path is None:
        images = "./_data/photos/dog/"  
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files] 
        img = random.choice(imgs)
    else:
        img = path[0]

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = quote_model(body, author)

    meme = Meme_Generator('./tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    return path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='gives a meme')
    parser.add_argument('--path', type=str, help='path to get images')
    parser.add_argument('--body', type=str, help='body of text to be in meme')
    parser.add_argument('--author', type=str, help='author of the text')
    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))