#!/usr/local/python3

from math import cos, sin, exp, pi
import os
import cairo

IMAGE_WIDTH_IN = 5
IMAGE_HEIGHT_IN = 5
DPI = 200
STROKE = .5

def makeImage(height, width, imageName):
    N = 500
    kA = 7
    kB = 8
 
    imageWidth = min(width, height)
    imageHeight = max(width, height)

    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, imageWidth, imageHeight)
    ctx = cairo.Context(surface)
    ctx.set_tolerance(.1)
    ctx.set_antialias(False)
    
    cx = imageWidth/2
    cy = imageHeight/2
    radius  = imageWidth/2 * .95
    
    # background
    ctx.set_source_rgb(1, 1, 1)
    ctx.rectangle(0, 0, imageWidth, imageHeight)
    ctx.fill()
    ctx.stroke()
    
    # lines
    ctx.set_line_width(STROKE)
    ctx.set_source_rgb(1, 0, 0)
    for d in range(N):
        angA = kA * d * 2 * pi / N
        angB = (kB * d) * 2 * pi / N
   
        x1 = cos(angA) * radius + cx
        y1 = sin(angA) * radius + cy
        x2 = cos(angB) * radius + cx
        y2 = sin(angB) * radius + cy

        ctx.move_to(x1, y1)
        ctx.line_to(x2, y2)
        ctx.stroke()
    
    surface.write_to_png(imageName)

if __name__ == "__main__":
    scriptName = os.path.basename(__file__)
    fileNum = scriptName[9 : len(scriptName)-3]
    imageName = 'image_{}.png'.format(fileNum)

    width = IMAGE_WIDTH_IN * DPI
    height = IMAGE_HEIGHT_IN * DPI
    makeImage(height, width, imageName)
