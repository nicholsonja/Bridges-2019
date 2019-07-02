import os
import numpy as np

from PIL import Image
from math import cos, sin

def saveImage(data, imageName, imageWidth, imageHeight, bg = None, fg = None):
    '''
    Convert and save data to PNG file. 
    '''
    maxCount = max(data)
    if bg == None:
        bg = [255, 255, 255]
    
    if fg == None:  
        fg = [  0,   0, 255]
    
    rgb = np.zeros((imageWidth, imageHeight, 3), 'uint8')
    for y in range(imageHeight):
        for x in range(imageWidth):
            cnt = data[y * imageWidth + x]
            alpha = min(cnt/maxCount * 10, 1.0)
                
            rgb[y, x, 0] = int(alpha * fg[0] + (1 - alpha) * bg[0] + .5)
            rgb[y, x, 1] = int(alpha * fg[1] + (1 - alpha) * bg[1] + .5)
            rgb[y, x, 2] = int(alpha * fg[2] + (1 - alpha) * bg[2] + .5)
    
    img = Image.fromarray(rgb)
    img.save(imageName)
    
def getImageName(sourceScriptName):
    scriptName = os.path.basename(sourceScriptName)
    fileNum = scriptName[9 : len(scriptName)-3]
    imageName = 'image_{}.png'.format(fileNum)
    return imageName

# Parametric equations

def circle(theta, radius, cx, cy):
    x = cos(theta) * radius + cx
    y = sin(theta) * radius + cy
    return (x, y)

def rose(theta, radius, petalK, cx, cy):
    '''
    Info: http://mathworld.wolfram.com/Rose.html
    '''
    x = cos(petalK * theta) * cos(theta) * radius + cx;
    y = cos(petalK * theta) * sin(theta) * radius + cy;
    return (x, y)

def lemniscate(theta, radius, cx, cy):
    '''
    Info: http://mathworld.wolfram.com/Lemniscate.html
    '''
    c = cos(theta)
    s = sin(theta)
    x = (radius * c)/(1 + s * s) + cx
    y = (radius * s * c)/(1 + s * s) + cy
    return (x, y)   
