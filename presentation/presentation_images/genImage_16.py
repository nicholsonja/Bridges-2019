#!/usr/local/python3

from helper import square

from math import cos, sin, exp, pi
import os
import cairo

IMAGE_WIDTH_IN = 5
IMAGE_HEIGHT_IN = 5
DPI = 100

STROKE = 10

def makeImage(height, width, imageName):
    imageWidth = min(width, height)
    imageHeight = max(width, height)

    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, imageWidth, imageHeight)
    ctx = cairo.Context(surface)
    ctx.set_tolerance(.1)
    ctx.set_antialias(False)
    
    cx = imageWidth/2
    cy = imageHeight/2
    radius  = imageWidth/2 * .65
    
    # background
    ctx.set_source_rgb(1, 1, 1)
    ctx.rectangle(0, 0, imageWidth, imageHeight)
    ctx.fill()
    ctx.stroke()
    
    
    # lines
    ctx.set_line_width(STROKE)
    ctx.set_source_rgb(0, 0, 0)

    N = 360
    for d in range(N+1):
        theta = d * 2 * pi / N 
        
        x, y = square(theta, radius, cx, cy, pi/4)

        if d == 0:
            ctx.move_to(x, y)
        else:
            ctx.line_to(x, y)
    ctx.stroke()
    surface.write_to_png(imageName)

if __name__ == "__main__":
    scriptName = os.path.basename(__file__)
    fileNum = scriptName[9 : len(scriptName)-3]
    imageName = 'image_{}.png'.format(fileNum)

    width = IMAGE_WIDTH_IN * DPI
    height = IMAGE_HEIGHT_IN * DPI
    makeImage(height, width, imageName)
