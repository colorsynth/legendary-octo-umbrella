#qpy:kivy
from PIL import Image, ImageFont, ImageDraw
import time
import math
import numpy

#font = ImageFont.truetype("/sdcard/fonts/Courier Code/CourierCode-Roman.ttf", 50)
#font = ImageFont.load_default()
t0=time.time()

picnum = 226
final = 1


if final ==1:
    xm = 1080
    ym = 1080
else:
    xm = 200
    ym = 200
'''
    xm = 1080
    ym = 1920
'''

im = Image.new ('RGB', (xm,ym), (1,1,1))
rN = numpy.ones((xm,ym))
gN = numpy.ones((xm,ym))
bN = numpy.ones((xm,ym))
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
for x0 in range (im.size[0]):
    x = (1*2*pi*(float (x0+1)/xm-h))*1
    for y0 in range (im.size[1]):
        y =(1*2*pi*(float (y0+1)/ym-h))*1
        z=complex (x,y)
        #z = complex (numpy.sin ((y+x)*numpy.sin (x)), numpy.sin ((x+y)*numpy.sin (y*y)))
        #z1 = complex (x+x, x*y)
        #zs = complex (numpy.sin (x*numpy.sin(x*y+numpy.sin (y))), numpy.sin(x*numpy.sin(x*y)))
        #z = complex (numpy.sin (numpy.sin (y*x)),x+numpy.sin (x*y))
        #z1= complex (numpy.sin (y*x),numpy.sin (numpy.sin (y)))
        #z=numpy.power(z,1.5)
        try:
            z = numpy.power (z, 10/(x+y))#*numpy.sin (x)
        except ZeroDivisionError:
            z = numpy.power (z, 7/00000000.1)
            
        m1=numpy.real (z)
        #m2=x+m1
        m2=numpy.imag (z)
        m3=numpy.angle (z)
        #numpy.sin (x*y)
        #m2=m1*numpy.sin(x)
        #m1=m1*m2
        #z=complex (z, z)+y
        #z=complex (z, z)
        #z=complex (z, z)
        #z=complex (z, z)
        if (abs (m1)>mMax):
            m1=1.0
            counts=counts+1
        if (abs (m2)>mMax):
            m2=1.0
        if (abs (m3)>mMax):
            m3=1.0
        bN[x0,y0] = numpy.sin (numpy.real (m1))
        gN[x0,y0] = numpy.sin (numpy.real (m2))
        rN[x0,y0] = numpy.sin (numpy.real (m3))
print counts 
print "overflows"
rN = numpy.nan_to_num(numpy.array((rN)))
gN = numpy.nan_to_num(numpy.array((gN)))
bN = numpy.nan_to_num(numpy.array((bN)))
'''
rN = numpy.real(numpy.fft.fft2 (rN))
gN = numpy.real(numpy.fft.fft2 (rN))
bN = numpy.real(numpy.fft.fft2 (rN))
'''
print rN.max ()
print rN.mean ()
rN -= rN.min ()
gN -= gN.min ()
bN -= bN.min ()
print rN.max ()
print gN.max ()
print bN.max ()


rN *= 255.0/rN.max()
bN *= 255.0/bN.max()
gN *= 255.0/gN.max()

for x0 in range (im.size[0]):
	for y0 in range (im.size[1]):
		p[x0,y0]  = (1*int(rN[x0,y0]), 1*int(gN[x0,y0]), 1*int(bN[x0,y0]))

#draw = ImageDraw.Draw(im)
#draw.text((10, 25), str ( time.clock ()-t) , font=font)

im = im.resize ((1080,1080),Image.NEAREST)

#im = im.resize ((640,640),Image.BILINEAR)

fd = open("ghostY_sir"+str (picnum).zfill (3)+".jpg","wb")
im.save (fd)
fd.close()
print (time.time ()-t0)
fd = open("likeaSir.py","rt")


if (final==1):
    fd2 = open ("allCode.txt","a")
    codes = fd.read()
    fd2.write ("\n\n\n***\ncode for: faceGrab" + str(picnum).zfill (3)+"\n***\n\n\n")
    fd2.write (codes)
    fd2.close ()
    fd.close ()