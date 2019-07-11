#!/usr/bin/env python3

from helper import hypotrochoid, circle, saveImage, getImageName
from math import pi, cos, sin
from random import uniform

IMAGE_WIDTH_IN = 5
IMAGE_HEIGHT_IN = 5
DPI = 200

def makeImage(height, width, imageName):
    kA = 101
    kB = 2
    numSamples = 1000000000
 
    imageWidth = width
    imageHeight = height

    data = [0] * imageHeight * imageWidth

    cx = imageWidth/2
    cy = imageHeight/2
    radius  = imageWidth/2

    circRadius = radius * .9
    hypoRadius = radius * .0275

    numSquares = 8
    squareRadius = radius/2

    for i in range(numSamples):
        theta = uniform(0, 2 * pi)
        
        pA_x, pA_y = circle(kA * theta, circRadius, cx, cy)
        pB_x, pB_y = hypotrochoid(kB * theta, hypoRadius,
                                   hypoRadius, 1/17 * hypoRadius, 1.1 * hypoRadius , cx, cy)
        
        # pick a random point on the line segment [pA, pB]
        r = uniform(0, 1)
        pC_x = (1 - r) * pA_x + r * pB_x
        pC_y = (1 - r) * pA_y + r * pB_y
        
        i = int(pC_x + .5)
        j = int(pC_y + .5)
        
        data[j * imageWidth + i] += 1
        
    saveImage(data, imageName, imageWidth, imageHeight,
              bg=[255, 255, 255], fg=[[0, 0, 255], [255, 0, 0]], alphaMultiplier=4)
    

if __name__ == "__main__":
    imageName = getImageName(__file__)
    
    width = IMAGE_WIDTH_IN * DPI
    height = IMAGE_HEIGHT_IN * DPI
    makeImage(height, width, imageName)
