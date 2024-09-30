from PIL import Image, ImageDraw,ImageFont
import PIL
import random
import math
import os
#array of all possible combination
alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

shapes=["circle","semicircle","quartercircle","triangle","rectangle","pentagon","star","cross"]

#20 training iterations
for i in range(20):
    for shape in shapes:
        for letter in alphabet:
            #random size, pos, dim
            dim=random.randint(100,1000)
            size=random.randint(15,math.floor(dim*0.5))
            posx=random.randint(10,math.floor(dim*0.9))
            posy=random.randint(10,math.floor(dim*0.9))
            #make sure the shape doesn't get cut off
            if posx<size:
                posx=size
            if size+posx>dim:
                posx=dim-size
            if posy<size:
                posy=size
            if size+posy>dim:
                posy=dim-size
        #create im object
            im = Image.new("RGB", size=(dim, dim))
#create draw object
            draw = ImageDraw.Draw(im)
            #grab font
            font = ImageFont.truetype("pt2/sans-serif.ttf", size)
            
            #polygonnnssssss
            if shape=="circle":
                draw.circle((posx,posy), size, fill=(random.randint(0,255),random.randint(0,255),random.randint(0,255)), outline=None, width=1)
            if shape=="semicircle":
                draw.pieslice([(posx-size,posy-size*1.4),(posx+size,posy+size*0.6)],0,180,fill=(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
            if shape=="quartercircle":
                draw.pieslice([(posx-size*1.4,posy-size*1.4),(posx+size*0.6,posy+size*0.6)],0,90,fill=(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
            if shape=="triangle":
                draw.regular_polygon((posx,posy,size),3,fill=(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
            if shape=="rectangle":
                draw.rectangle([(posx-size,posy-size),(posx+size,posy+size)],fill=(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
            if shape=="pentagon":
                draw.regular_polygon((posx,posy,size),5,fill=(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
            if shape=="star":
                tengon=[]
                #basically 10 a ten sided polygon with some points "collapsed"
                for n in range(0,5):
                    #generate outer point
                    x = size*math.cos(math.radians(-90+n*72))+posx
                    y = size*math.sin(math.radians(-90+n*72))+posy
                    #generate concave point
                    inx = size/2.6*math.cos(math.radians(-54+n*72))+posx
                    iny = size/2.6*math.sin(math.radians(-54+n*72))+posy
                    #append to coord list
                    tengon.append((x,y))
                    tengon.append((inx,iny))
                    draw.polygon(tengon,fill=(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
            if shape=="cross":
                #two lines but thicc
                fillcolor=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
                draw.line([(posx,posy+size/1.5),(posx,posy-size/1.5)],fill=fillcolor,width=math.floor(size/2))
                draw.line([(posx+size/1.5,posy),(posx-size/1.5,posy)],fill=fillcolor,width=math.floor(size/2))

                    


                    
                
                
            
            #add text and rotate
            draw.text((posx, posy),letter,(255,255,255),font=font,anchor="mm")
            im=im.rotate(random.randint(0,360))
            
            im.save(f"pt2/data/train/{shape} {letter}/{i}.jpg")

#ditto, but in a diff folder
for i in range(20):
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
        
            im = Image.new("RGB", size=(dim, dim))

            draw = ImageDraw.Draw(im)
            font = ImageFont.truetype("pt2/sans-serif.ttf", size)
            
            #polygonnnssssss
            if shape=="circle":
                draw.circle((posx,posy), size, fill=(random.randint(0,255),random.randint(0,255),random.randint(0,255)), outline=None, width=1)
            if shape=="semicircle":
                draw.pieslice([(posx-size,posy-size*1.4),(posx+size,posy+size*0.6)],0,180,fill=(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
            if shape=="quartercircle":
                draw.pieslice([(posx-size*1.4,posy-size*1.4),(posx+size*0.6,posy+size*0.6)],0,90,fill=(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
            if shape=="triangle":
                draw.regular_polygon((posx,posy,size),3,fill=(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
            if shape=="rectangle":
                draw.rectangle([(posx-size,posy-size),(posx+size,posy+size)],fill=(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
            if shape=="pentagon":
                draw.regular_polygon((posx,posy,size),5,fill=(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
            if shape=="star":
                pentagon=[]
                
                for n in range(0,5):
                    #generate outer point
                    x = size*math.cos(math.radians(-90+n*72))+posx
                    y = size*math.sin(math.radians(-90+n*72))+posy
                    #generate concave point
                    inx = size/2.6*math.cos(math.radians(-54+n*72))+posx
                    iny = size/2.6*math.sin(math.radians(-54+n*72))+posy
                    #append to coord list
                    pentagon.append((x,y))
                    pentagon.append((inx,iny))
                    draw.polygon(pentagon,fill=(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
            if shape=="cross":
                fillcolor=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
                draw.line([(posx,posy+size/1.5),(posx,posy-size/1.5)],fill=fillcolor,width=math.floor(size/2))
                draw.line([(posx+size/1.5,posy),(posx-size/1.5,posy)],fill=fillcolor,width=math.floor(size/2))

                    


                    
                
                
            

            draw.text((posx, posy),letter,(255,255,255),font=font,anchor="mm")
            im=im.rotate(random.randint(0,360))
            
            im.save(f"pt2/data/val/{shape} {letter}/{i}.jpg")

                
                

            

