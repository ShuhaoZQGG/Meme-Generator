from PIL import Image, ImageDraw, ImageFont
import os
from random import randint
import numpy as np
from numpy.random import f

class Meme_Generator:
    def __init__(self,output_dir):
        self.output_dir = output_dir
        os.makedirs(self.output_dir,exist_ok=True)

    def make_meme(self,img_path,text,author,width=500)->str:
        img = Image.open(img_path)
        if width <= 500:
            ratio = width/float(img.size[0])
            height = int(ratio*float(img.size[1]))
            img = img.resize((width,height),Image.NEAREST)
        else:
            raise ValueError('Width cannot exceed 500')
        
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf', size=20)
        meme = f'{text}{author}'
        color = list(np.random.choice(range(256), size=3))
        draw = draw.text((randint(0,len(meme))),meme,font=font,fill=color)
       
        out_path = os.path.join(self.output_dir,f'{text}{author}_{randint(0,100000)}.jpg')
        img.save(out_path)
        return out_path
        
