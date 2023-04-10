import turtle

n = int(input("please enter an integer to draw a n-gon: "))

sides = 100
angle = (n-2)*180
for i in range (n):
    turtle.forward(sides)
    turtle.left(180-angle/n)
turtle.done()
