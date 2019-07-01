#!/usr/bin/env python3

import multiprocessing

from helper import circle, saveImage, getImageName
from math import pi
from random import uniform

IMAGE_WIDTH_IN = 5
IMAGE_HEIGHT_IN = 5
DPI = 100

def initializeData(imageWidth, imageHeight):
    return [0] * imageHeight * imageWidth

def computeData(processId, imageWidth, imageHeight, numSamples, kA, kB):
    data = initializeData(imageWidth, imageHeight)

    cx = imageWidth/2
    cy = imageHeight/2
    radius  = imageWidth/2 * .85

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
    
    print("Finished process {}".format(processId))
    return data
    
def runDataCalculations(imageWidth, imageHeight, numSamples, kA, kB):
    totalNumProcesses = 10
    numSamplesPerProcess = int(numSamples / totalNumProcesses)
    
    data = initializeData(imageWidth, imageHeight)
    
    def saveData(remoteData):
        for i in range(len(data)):
            data[i] += remoteData[i]
            
    # number of running processes depends on os.cpu_count() 
    pool = multiprocessing.Pool() 
    for i in range(totalNumProcesses):
        pool.apply_async(computeData,
                         args=(i, imageWidth, imageHeight, numSamplesPerProcess, kA, kB),
                         callback = saveData)
    pool.close()
    pool.join()
    
    return data

def makeImage(height, width, imageName):
    kA = 4
    kB = 7
    numSamples = 100000000
 
    imageWidth = min(width, height)
    imageHeight = max(width, height)

    data = runDataCalculations(imageWidth, imageHeight, numSamples, kA, kB)
        
    saveImage(data, imageName, imageWidth, imageHeight)
    
if __name__ == "__main__":
    imageName = getImageName(__file__)
    
    width = IMAGE_WIDTH_IN * DPI
    height = IMAGE_HEIGHT_IN * DPI
    makeImage(height, width, imageName)
