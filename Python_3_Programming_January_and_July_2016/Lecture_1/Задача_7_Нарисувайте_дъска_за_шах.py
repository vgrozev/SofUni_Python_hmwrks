import turtle

# side=40
# turtle.speed('fastest')
#
# for i in range(8):
#     for z in range(8):
#         if (i % 2==0 and z % 2 == 0) or (i % 2 != 0 and z % 2 != 0):
#             turtle.begin_fill()
#         for y in range(4):
#             turtle.forward(side)
#             turtle.left(90)
#         turtle.end_fill()
#         turtle.forward(side)
#
#     turtle.penup()
#     turtle.goto(0,side + (side * i))
#     turtle.pendown()
#
# turtle.exitonclick()

side = 40
turtle.speed('fastest')

for row in range(8):
    for column in range(8):
        if ((column + row) % 2 == 0):
            turtle.begin_fill()
        for _ in range(4):
            turtle.forward(side)
            turtle.left(90)

        turtle.end_fill()
        turtle.forward(side)

    turtle.penup()
    turtle.goto(0,-(side + (side * row)))
    turtle.pendown()

turtle.exitonclick()