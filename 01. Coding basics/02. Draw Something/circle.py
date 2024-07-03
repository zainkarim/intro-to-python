# DRAW A CIRCLE
import drawsvg as draw

d = draw.Drawing(200, 200, origin = 'center')
d.append(draw.Circle(0,0,30)) # render a circle
d.save_svg('output.svg')