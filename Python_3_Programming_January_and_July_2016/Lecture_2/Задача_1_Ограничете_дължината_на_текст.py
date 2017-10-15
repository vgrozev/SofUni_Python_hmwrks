user_input = input("Please, enter your string: ")
if len(user_input) < 10:
    print(user_input)
else:
    print(user_input[:10] + '...')

