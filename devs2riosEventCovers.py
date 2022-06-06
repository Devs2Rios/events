'''Event cover generator for DrawBot'''
# Modules
import os
from datetime import datetime
# Paths
user = os.path.expanduser('~')
desktop = os.path.join(user,'Desktop')
# Pre-design values
size(800,400)
w, h = width(), height()
xblocks, yblocks = 100, 50 
xsize, ysize = w/xblocks, h/yblocks
x, y = 0, 0
# Random color value method
def rCl(): return randint(0,255)/255
# Design loop
while x < w:
    while y < h:
        rectColor = rCl(),rCl(),rCl()
        with savedState():
            fill(*rectColor)
            stroke(*rectColor)
            strokeWidth(0.1)
            translate(x,y)
            rect(0,0,xsize,ysize)
        y += ysize
    x += xsize
    y = 0
# Export callings
timestamp = datetime.now().strftime('%Y-%m-%d')
saveImage(os.path.join(desktop,f'devs2rios-event-cover-{timestamp}.png'))
