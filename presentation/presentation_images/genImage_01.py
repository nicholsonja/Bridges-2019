#!/usr/local/python3

from math import cos, sin, exp, pi
import os
import cairo

IMAGE_WIDTH_IN = 5
IMAGE_HEIGHT_IN = 5
DPI = 300

STROKE = 5

def drawDot(d, N, textRadius, cx, cy, radius, ctx):
        ang1 = d * 2 * pi / N
        x1 = cos(ang1) * textRadius + cx
        y1 = sin(ang1) * textRadius + cy

        text = str(d)
        (x_bearing, y_bearing, t_width, t_height, x_advance, y_advance) = ctx.text_extents(text)
        ctx.move_to(x1 - t_width/2, y1 + t_height/2)
        ctx.show_text("{}".format(d))
        ctx.stroke()

        x1 = cos(ang1) * radius + cx
        y1 = sin(ang1) * radius + cy
        ctx.arc(x1, y1, 15, 0, 2 * pi)
        ctx.fill()

def makeImage(height, width, imageName):
    N = 30
    k = 2
 
    imageWidth = min(width, height)
    imageHeight = max(width, height)

    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, imageWidth, imageHeight)
    ctx = cairo.Context(surface)
    ctx.set_tolerance(.1)
    ctx.set_antialias(False)
    
    cx = imageWidth/2
    cy = imageHeight/2
    drawing_width = imageWidth
    radius  = drawing_width/2 
    textRadius = radius * .95
    radius = radius * .85
    
    # background
    ctx.set_source_rgb(0xfc/255, 0xfc/255, 0xfc/255)
    ctx.rectangle(0, 0, imageWidth, imageHeight)
    ctx.fill()
    ctx.stroke()
    
    # circle
    ctx.set_source_rgb(1, .5, .5)
    ctx.set_line_width(STROKE)
    ctx.arc(cx, cy, radius, 0, 2 * pi)
    ctx.stroke()
    
    # lines
    ctx.set_source_rgb(0, 0, 1)
    for d in range(N):
        ang1 = d * 2 * pi / N
        ang2 = (k * d) * 2 * pi / N
   
        x1 = cos(ang1) * radius + cx
        y1 = sin(ang1) * radius + cy
        x2 = cos(ang2) * radius + cx
        y2 = sin(ang2) * radius + cy

        ctx.move_to(x1, y1)
        ctx.line_to(x2, y2)
        ctx.stroke()
    
    #dots
    ctx.set_source_rgb(0, 0, 0)
    ctx.set_font_size(50)
    for d in range(N):
        drawDot(d, N, textRadius, cx, cy, radius, ctx)
    
    surface.write_to_png(imageName)

if __name__ == "__main__":
    scriptName = os.path.basename(__file__)
    fileNum = scriptName[9 : len(scriptName)-3]
    imageName = 'image_{}.png'.format(fileNum)

    width = IMAGE_WIDTH_IN * DPI
    height = IMAGE_HEIGHT_IN * DPI
    makeImage(height, width, imageName)
