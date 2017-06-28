import turtle

user_input = input("Please enter the lenght of the side: ")
length = int(user_input)

turtle.speed('slow')

for _ in range(0, 4):
    turtle.forward(length)
    turtle.right(90)

turtle.done()

