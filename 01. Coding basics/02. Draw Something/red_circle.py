import drawsvg as draw

d = draw.Drawing(200,200, origin = 'center') # create canvas
d.append(draw.Circle(0, 0, 50,
            fill = 'red', stroke_width = 1, stroke = 'black')) # render a circle

d