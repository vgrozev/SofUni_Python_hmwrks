"""
Първи текст: This is soo difficult, I prefer playing WoW
Втори текст: soo
Резултат: difficult, I preffer playing WoW
"""
user_input1 = input("Please enter the first string: ")
user_input2 = input("Please enter the substring: ")

if user_input2 == '':
    print("the second input must not be empty string!")
elif user_input2 in user_input1:
    print(user_input1.split(user_input2)[1].lstrip())
else:
    print("Substring is not found")
