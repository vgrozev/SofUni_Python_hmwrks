import turtle

user_length = input("Please enter the length of the side: ")
length = int(user_length)
user_degrees = input("Please enter the angle: ")
degrees = int(user_degrees)

turtle.speed('slow')

while True:
    turtle.forward(length)
    turtle.right(degrees)

turtle.done()