import os
import numpy as np

from PIL import Image
from math import cos, sin, tan, pi, sqrt

SINGLE_COLOR = 1
GRADIENT_COLOR = 2

def saveImage(data, imageName, imageWidth, imageHeight, 
              bg = None, fg = None, alphaMultiplier = 10):
    '''
    Convert and save data to PNG file. 

    bg : background color. Three item tuple with integers from 0 - 255
    fg : forground color. A list with integers from 0 - 255, e.g. [255, 128, 0],
         which colors the entire shape based on alpha values computed from counts.
         Or a list of two 3-items lists, e.g. [[255, 0, 0], [0, 0, 255]],
         which is used to computer a gradient of colors, which is then is 
         used to color the entire shape based on alpha values computed from counts.
    alphaMultiplier : stretches counts so that lower counts can be perceived
    '''
    maxCount = max(data)

    drawStyle = SINGLE_COLOR
    if bg == None:
        bg = [255, 255, 255]

    
    if fg == None:  
        fg = [  0,   0, 255]
    elif type(fg[0]) in (list, tuple):
        drawStyle = GRADIENT_COLOR
        cx = imageWidth / 2
        cy = imageHeight / 2
        radius = min(imageWidth, imageHeight)/2

    
    rgb = np.zeros((imageHeight, imageWidth, 3), 'uint8')
    for y in range(imageHeight):
        for x in range(imageWidth):
            cnt = data[y * imageWidth + x]
            alpha = min(cnt/maxCount * alphaMultiplier, 1.0)
               
            if drawStyle == SINGLE_COLOR:
                color = fg
            elif drawStyle == GRADIENT_COLOR:
                # compute distance from center of bitmap
                px = x - cx;
                py = y - cy;
            
                px = px / radius;
                py = py / radius;
            
                dist = sqrt(pow(px, 2) + pow(py, 2))
           
                # use distance to weight the two colors
                color = [
                    int(dist * fg[0][0] + (1 - dist) * fg[1][0] + .5),
                    int(dist * fg[0][1] + (1 - dist) * fg[1][1] + .5),
                    int(dist * fg[0][2] + (1 - dist) * fg[1][2] + .5)
                ]

            rgb[y, x, 0] = int(alpha * color[0] + (1 - alpha) * bg[0] + .5)
            rgb[y, x, 1] = int(alpha * color[1] + (1 - alpha) * bg[1] + .5)
            rgb[y, x, 2] = int(alpha * color[2] + (1 - alpha) * bg[2] + .5)
            
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

def rose(theta, radius, n, cx, cy):
    '''
    Info: http://mathworld.wolfram.com/Rose.html
    '''
    x = cos(n * theta) * cos(theta) * radius + cx
    y = cos(n * theta) * sin(theta) * radius + cy
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

def hypocycloid(theta, radius, R, r, cx, cy):
    '''
    Info: http://mathworld.wolfram.com/Hypocycloid.html

    R: outer circle radius
    r: inner circle radius
    '''
    x = ((R-r) * cos(theta) + r * cos((R-r)/r * theta)) * radius + cx
    y = ((R-r) * sin(theta) - r * sin((R-r)/r * theta)) * radius + cx
    return (x, y)  

def hypotrochoid(theta, radius, R, r, d, cx, cy):
    '''
    Info: http://mathworld.wolfram.com/Hypotrochoid.html

    R: outer circle radius
    r: inner circle radius
    d: distance from the center of the interior circle. 
    '''
    x = ((R-r) * cos(theta) + d * cos((R-r)/r * theta)) * radius + cx
    y = ((R-r) * sin(theta) - d * sin((R-r)/r * theta)) * radius + cx
    return (x, y)  

def square(theta, radius, cx, cy, rotAng = 0):
    '''
    One way to do a square with a parametric equation.

    rotAng : radians. Rotates the square
    '''
    n = int (theta / (2 * pi))
    theta = theta - n * 2 * pi
    if theta < 0:
        theta += 2 * pi

    if theta >= pi / 4 and theta < 3 * pi / 4:
        x = cos(theta)/sin(theta)
        y = 1
    elif theta >= 3 * pi / 4 and theta < 5 * pi / 4:
        x = -1
        y = -tan(theta)
    elif theta >= 5 * pi / 4 and theta < 7 * pi / 4:
        x = -cos(theta)/sin(theta)
        y = -1
    else:
        x = 1
        y = tan(theta)

    x1 = x * radius
    y1 = y * radius

    x = x1 * cos(rotAng) - y1 * sin(rotAng) +  cx
    y = y1 * cos(rotAng) + x1 * sin(rotAng) +  cy

    return x, y

