is_even = False

while not is_even:
    num = float(input("Enter even number: "))

    if num % 2 == 0:
        is_even = True
        print("Even number entered: {0:g}".format(num))
    else:
        print("Invalid number!")
        print("The number is not even.")
