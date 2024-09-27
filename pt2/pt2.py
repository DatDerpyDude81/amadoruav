from PIL import Image, ImageDraw,ImageFont
import PIL
import random
import math
import ultralytics
alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

shapes=["circle","semicircle","quartercircle","triangle","rectangle","pentagon","star","cross"]
for shape in shapes:
    for letter in alphabet:
        dim=random.randint(100,1000)
        size=random.randint(15,math.floor(dim*0.5))
        posx=random.randint(10,math.floor(dim*0.9))
        posy=random.randint(10,math.floor(dim*0.9))
        if posx<size:
            posx=size
        if size+posx>dim:
            posx=dim-size
        if posy<size:
            posy=size
        if size+posy>dim:
            posy=dim-size
    
        im = Image.new(mode="RGB", size=(dim, dim))

        draw = ImageDraw.Draw(im)
        font = ImageFont.truetype("pt2/sans-serif.ttf", size)
        if shape=="circle":
            draw.circle((posx,posy), size, fill=(random.randint(0,255),random.randint(0,255),random.randint(0,255)), outline=None, width=1)
        if shape=="semicircle":
            draw.pieslice([(posx-size,posy-size*1.5),(posx+size,posy+size*0.5)],0,180,fill=(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        if shape=="quartercircle":
            draw.pieslice([(posx-size*1.4,posy-size*1.4),(posx+size*0.6,posy+size*0.6)],0,90,fill=(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
            
        

        draw.text((posx, posy),letter,(255,255,255),font=font,anchor="mm")

        im.save(f"{letter}{shape}.jpg")

        

