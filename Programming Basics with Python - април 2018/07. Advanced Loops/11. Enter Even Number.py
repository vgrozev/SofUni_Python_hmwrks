is_even = False

while not is_even:
    num = float(input("Enter even number: "))

    if num % 2 == 0:
        is_even = True
        print("Even number entered: {0:g}".format(num))
    elif num % 2 != 0:
        print("The number is not even.")
    else:
        print("Invalid number!")
