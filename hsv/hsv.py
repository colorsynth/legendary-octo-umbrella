#qpy:kivy
from PIL import Image, ImageFont, ImageDraw
import time
import math
import numpy

#font = ImageFont.truetype("/sdcard/fonts/Courier Code/CourierCode-Roman.ttf", 50)
#font = ImageFont.load_default()
t0=time.time()

picnum = 243
final = 0


if final ==1:
    xm = 1080
    ym = 1080
else:
    xm = 1080
    ym = 50
'''
    xm = 1080
    ym = 1920
'''

im = Image.new ('RGB', (xm,ym), (1,1,1))

draw = ImageDraw.Draw(im)
#draw.text((10, 25), str (42) , font=font, fill=(20,20,20))


p = im.load ()
pi = math.pi
z=0.5
h=0.5#.5-0.25
m1=1.0
m2=1.0
m3=1.0
mMax=9999999999999999
counts=0
hue = 1
saturation = 100
luminance = 50
factorZ = 1
theta = pi/2
for x0 in range (im.size[0]):
    xi = (1*2*pi*(float (x0+1)/xm-h))*1
    for y0 in range (im.size[1]):
        yi =(1*2*pi*(float (y0+1)/ym-h))*1
        x=xi*numpy.cos (theta) - yi*numpy.sin (theta)
        y=xi*numpy.sin (theta) + yi*numpy.cos (theta)
        
        z=complex  (x,y)
        zs=complex (numpy.sin (y),numpy.sin (x))
        z1=numpy.power (zs*z,1.5)*x*numpy.sin (y)#numpy.power ( (x*numpy.sin (y)+y)*zs,0.75)
        z2=zs
        hue =  ( (factorZ*numpy.abs (z1)))%1
        hue=(int) ((hue)*360)
        #saturation = (int) (50*(factorZ*numpy.sin (numpy.abs (z2))+1))
        lf=30
        ls=0
        #luminance = (int) (ls+(lf)*(numpy.sin (numpy.abs (z2))+1))
        
        
        color = 'hsl(%d, %d%%, %d%%)' % (hue, saturation, luminance)
        #im.putpixel((1,1),(1,1,1))#color)
        draw.point ((x0,y0),fill=color)
        

im = im.resize ((1080,1080),Image.NEAREST)

#im = im.resize ((640,640),Image.BILINEAR)

fd = open("hsV"+str (picnum).zfill (3)+".jpg","wb")
im.save (fd)
fd.close()
print (time.time ()-t0)
fd = open("hsv.py","rt")


if (final==1):
    fd2 = open ("allCodehsv.txt","a")
    codes = fd.read()
    fd2.write ("\n\n\n***\ncode for: hsv" + str(picnum).zfill (3)+"\n***\n\n\n")
    fd2.write (codes)
    fd2.close ()
    fd.close ()