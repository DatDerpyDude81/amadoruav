from PIL import Image, ImageDraw,ImageFont
import random
import ultralytics
alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
dim=random.randint(100,1000)
shapes=["circle","semicircle" "quarter circle","triangle","rectangle","pentagon","star","cross"]
for shape in shapes:
    for letter in alphabet:
        posx=random.randint(10,dim-20)
        posy=random.randint(10,dim-20)
        size=random.randint(15,50)
        im = Image.new(mode="RGB", size=(dim, dim))
        draw = ImageDraw.Draw(im)
        font = ImageFont.truetype("pt2/sans-serif.ttf", size)
        draw.text((posx, posy),letter,(255,255,255),font=font)
        im=im.rotate(random.randint(0,360))
        im.save(f"{letter}{shape}.jpg")

        

