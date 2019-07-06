#!/usr/bin/env python3

from helper import circle, rose, saveImage, getImageName
from math import pi
from random import uniform

IMAGE_WIDTH_IN = 5
IMAGE_HEIGHT_IN = 5
DPI = 200

def makeImage(height, width, imageName):
    kA = 2
    kB = 3
    numSamples = 100000000
 
    imageWidth = width
    imageHeight = height

    data = [0] * imageHeight * imageWidth

    cx = imageWidth/2
    cy = imageHeight/2
    radius  = imageWidth/2 * .95

    radius2 = radius * .9

    for i in range(numSamples):
        theta = uniform(0, 32 * pi)
        
        pA_x, pA_y = rose(kA * theta, radius, 4/5, cx, cy)
        pB_x, pB_y = rose(kB * theta, radius2, 2/5, cx, cy)
        
        # pick a random point on the line segment [pA, pB]
        r = uniform(0, 1)
        pC_x = (1 - r) * pA_x + r * pB_x
        pC_y = (1 - r) * pA_y + r * pB_y
         
        i = int(pC_x + .5)
        j = int(pC_y + .5)
        
        data[j * imageWidth + i] += 1
        
    saveImage(data, imageName, imageWidth, imageHeight,
              bg=[255, 255, 255], fg=[0x6A, 0x47, 0], alphaMultiplier=5)
    

if __name__ == "__main__":
    imageName = getImageName(__file__)
    
    width = IMAGE_WIDTH_IN * DPI
    height = IMAGE_HEIGHT_IN * DPI
    makeImage(height, width, imageName)
