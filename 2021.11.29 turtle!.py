#반복문을 사용해서 거북이가 도형을 그리는 프로그램

import turtle

turtle.shape("turtle")
turtle.color("dark gray")
turtle.bgcolor("black")

for R in range(4):
    turtle.forward(100)
    turtle.left(90)

turtle.up()
turtle.goto(200,200)
turtle.down()

turtle.color("red")

for R in range(3):
    turtle.forward(50)
    turtle.left(120)

turtle.up()
turtle.goto(-250,200)
turtle.down()

turtle.color("light blue")

for R in range(5):
    turtle.forward(75)
    turtle.left(72)

turtle.up()
turtle.goto(-250,-200)
turtle.down()

turtle.color("white")

for R in range(6):
    turtle.forward(120)
    turtle.left(60)

turtle.up()
turtle.goto(200,-200)
turtle.down()

turtle.color('yellow')

for R in range(5):
    turtle.forward(100)
    turtle.right(144)
