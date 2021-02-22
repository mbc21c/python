# coding : utf-8

from PIL import Image, ImageDraw, ImageFont
import textwrap
from random import *
import os

def run(astr):
    para = textwrap.wrap(astr, width=11)
    MAX_W, MAX_H = 480, 480
    r = randrange(255)
    g = randrange(255)
    b = randrange(255)

    bg_color = 'rgb(' + str(r) + ',' + str(g) +',' + str(b) + ')'
    im = Image.new('RGB', (MAX_W, MAX_H), bg_color)
    draw = ImageDraw.Draw(im)
    font_folder = os.path.dirname(os.path.realpath(__file__))
    selectFont = ImageFont.truetype(font_folder + '/CookieRun Regular.ttf',46)

    if r+g+b > 320 :
        font_color = 'rgb(0,0,0)'
    else :
        font_color = 'rgb(255,255,255)'

    current_h, pad = 200, 10
    for line in para:
        w, h = draw.textsize(line,font=selectFont)
        draw.text(((MAX_W - w) /2, current_h), line, fill=font_color, font=selectFont)
        current_h += h + pad

    im.save( '{}.png'.format(astr[:8]))
    return

if __name__ == "__main__":
    astr = input("제목을 입력하세요 : ")
    run(astr)
    print("done")