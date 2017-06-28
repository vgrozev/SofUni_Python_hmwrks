
user_input = input("Please enter the full name: ")
#user_input = "Fdafa uadfaf Gafasdf"

abrv = [name[:1] for name in user_input.split()]
print('.'.join(abrv).upper() + '.')
