#!/usr/bin/env python3

from helper import rose, circle, saveImage, getImageName
from math import pi
from random import uniform

IMAGE_WIDTH_IN = 5
IMAGE_HEIGHT_IN = 5
DPI = 100

def makeImage(height, width, imageName):
    kA = 1
    kB = 2
    numSamples = 100000000
 
    imageWidth = min(width, height)
    imageHeight = max(width, height)

    data = [0] * imageHeight * imageWidth

    cx = imageWidth/2
    cy = imageHeight/2
    radius  = imageWidth/2 * .85

    for i in range(numSamples):
        # Note: using 10 * pi.  If only 2 * pi, whole image is not drawn
        theta = uniform(0, 10 * pi)
        
        pA_x, pA_y = rose(kA * theta, radius * .9, 1.2, cx, cy)
        pB_x, pB_y = circle(kB * theta, radius, cx, cy)

        # pick a random point on the line segment [pA, pB]
        r = uniform(0, 1)
        pC_x = (1 - r) * pA_x + r * pB_x
        pC_y = (1 - r) * pA_y + r * pB_y
        
        i = int(pC_x + .5)
        j = int(pC_y + .5)
        
        data[j * imageWidth + i] += 1
        
    saveImage(data, imageName, imageWidth, imageHeight)
    

if __name__ == "__main__":
    imageName = getImageName(__file__)
    
    width = IMAGE_WIDTH_IN * DPI
    height = IMAGE_HEIGHT_IN * DPI
    makeImage(height, width, imageName)
