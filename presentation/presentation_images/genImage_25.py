#!/usr/bin/env python3

import re

from helper import circle, saveImage, getImageName
from math import pi
from random import uniform

IMAGE_WIDTH_IN = 5
IMAGE_HEIGHT_IN = 5
DPI = 200

def makeImage(height, width, imageName):
    kA = 7.9
    kB = 11
    numSamples = 100000
 
    imageWidth = min(width, height)
    imageHeight = max(width, height)

    for numSamples in (100000, 100000000):

        data = [0] * imageHeight * imageWidth

        cx = imageWidth/2
        cy = imageHeight/2
        radius  = imageWidth/2 * .95

        for i in range(numSamples):
            theta = uniform(0, 2 * pi)
            
            pA_x, pA_y = circle(kA * theta, radius, cx, cy)
            pB_x, pB_y = circle(kB * theta, radius, cx, cy)
        
            # pick a random point on the line segment [pA, pB]
            r = uniform(0, 1)
            pC_x = (1 - r) * pA_x + r * pB_x
            pC_y = (1 - r) * pA_y + r * pB_y
            
            i = int(pC_x + .5)
            j = int(pC_y + .5)
            
            data[j * imageWidth + i] += 1
            
        imageNameCnt = re.sub(r"image", f"image_{numSamples}", imageName)

        saveImage(data, imageNameCnt, imageWidth, imageHeight,
                    bg=[255, 255, 255], fg=[0, 0, 0])
    

if __name__ == "__main__":
    imageName = getImageName(__file__)
    
    width = IMAGE_WIDTH_IN * DPI
    height = IMAGE_HEIGHT_IN * DPI
    makeImage(height, width, imageName)
