from PIL import Image, ImageDraw, ImageFont
import os
import random
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
        
        length = len(text) + len(author)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype('arial.ttf', size=20)
        meme = f'{text}{author}'
        color = 'white'
        draw.text((randint(0,length),randint(0,length)),meme,font=font,fill=color)
       
        out_path = r'{}/{}.png'.format(self.output_dir,random.randint(0, 1000))
        img.save(out_path)
        return out_path
        
