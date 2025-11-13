from myFunctions import *
from random import randint
turtle.colormode(255)

turtle.tracer(0)


turtle.bgcolor("black")
for times in range( 256):
  c = ( 255 - times, 0, 255 - times )
  bob.color("black", c)
  polygon(10, 200, c )
  bob.forward(times * 2)
  bob.left(9)
  
bob.home()

for times in range ( 256 ):
  c = ( 0 , 0 , 255-times)
  bob.color("black", c)
  polygon(10, 100, c)
  bob.forward(times * 2)
  bob.left(9)

bob.home()

for times in range ( 256 ):
  c = ( 255-times  , 0  , 255-times)
  bob.color("black", c)
  polygon(10, 50, c)
  bob.forward(times * 2)
  bob.left(9)

bob.home()

for times in range ( 256 ):
  c = ( 0  , 0  , 255-times)
  bob.color("black", c)
  polygon(10, 25, c)
  bob.forward(times * 2)
  bob.left(9)

bob.home()

for times in range ( 256 ):
  c = (255-times, 0, 255-times)
  bob.color("black", c)
  polygon(10,12.5, c)
  bob.forward(times * 2)
  bob.left(9)

bob.home()

for times in range ( 256 ):
  c = (0, 0, 255-times)
  bob.color("black", c)
  polygon(10, 6.25, c)
  bob.forward(times * 2)
  bob.left(9)

bob.home()

for times in range ( 256 ):
  c = (255-times, 0, 255-times)
  bob.color("black", c)
  polygon(10,3.125, c)
  bob.forward(times * 2)
  bob.left(9)
