import turtle

i = 15
l = 20
while True:
    turtle.left(i % 17)
    turtle.forward(l / 2)

    if l < 12:
        l = 33
    l += 1

turtle.done()
