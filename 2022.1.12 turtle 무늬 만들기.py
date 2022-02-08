import turtle
turtle.shape('turtle')
turtle.color('gray')
turtle.bgcolor('black')

#for x in range(360,0,-1):
 #    turtle.forward(10)
#     turtle.left(x)

for x in range(200,0,-1):
    turtle.forward(x)
    turtle.left(65)

turtle.up()
turtle.goto(300,300)
turtle.color('black')
