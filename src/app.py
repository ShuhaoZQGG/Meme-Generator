import random
import os
import requests
from flask import Flask, render_template, request
from MemeEngine import Meme_Generator
from QuoteEngine import Ingestor, quote_model
# @TODO Import your Ingestor and MemeEngine classes

app = Flask(__name__)

meme = Meme_Generator('./static')


def setup():
    """ Load all resources """

    quote_files = [
            "./_data/DogQuotes/DogQuotesTXT.txt",
            "./_data/DogQuotes/DogQuotesDOCX.docx",
            "./_data/DogQuotes/DogQuotesPDF.pdf",
            "./_data/DogQuotes/DogQuotesCSV.csv"]
    
    images_path = "./_data/photos/dog/"

    # TODO: Use the Ingestor class to parse all files in the
    # quote_files variable
    quotes = []
    for f in quote_files:
        if not os.path.exists(f):
            print(f"The following quote sample is missing: {f}")
            continue
        quotes.extend(Ingestor.parse(f))

    if not quotes:
        raise Exception("No sample quotes found!")

    # TODO: Use the pythons standard library os class to find all
    # images within the images images_path directory
    imgs =[]
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]


    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    # @TODO:
    # Use the random python standard library class to:
    # 1. select a random image from imgs array
    # 2. select a random quote from the quotes array

    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    # @TODO:
    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.
    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form paramaters.
    # 3. Remove the temporary saved image.
    img_url = request.form('img_url')
    response = requests.get(img_url)
    quote = quote_model(request.form['body'],request.form['author'])
    img_path_tmp = f'./tmp/img_temp_{random.randint(0,1000000)}.jpg'
    
    with open(img_path_tmp,'wb') as file:
        file.write(response.content)

    path = meme.make_meme(img_path_tmp, quote.body, quote.author)

    os.remove(img_path_tmp)
    
    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
