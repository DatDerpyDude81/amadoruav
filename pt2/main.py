from PIL import Image, ImageDraw,ImageFont
import random
import ultralytics
alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



for letter in alphabet:
    im = Image.new(mode="RGB", size=(200, 200))
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("pt2/sans-serif.ttf", random.randint(20,40))
    draw.text((0, 0),letter,(255,255,255),font=font)
    im.save(f"{letter}.jpg")
                              
