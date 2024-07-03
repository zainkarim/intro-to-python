# draw a simple house
import drawsvg as draw

d = draw.Drawing(200, 200, origin='center')

d.append(draw.Rectangle(0,-100,100,100, fill='gray', stroke='black')) # body of house

d.append(draw.Lines(0,0, 100,0, 50,50, close=True, fill='green', stroke='black')) # roof

d.append(draw.Rectangle(40,-100,20,50, fill='red', stroke='black')) # door

d.append(draw.Rectangle(15,-30,15,15, fill='white', stroke='black')) # left window
d.append(draw.Rectangle(70,-30,15,15, fill='white', stroke='black')) # right window

d.save_svg('house.svg')