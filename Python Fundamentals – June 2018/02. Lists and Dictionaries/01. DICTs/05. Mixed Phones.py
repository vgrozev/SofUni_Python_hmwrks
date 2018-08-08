raw_data = input()

phonebook = {}

while raw_data != "Over":

    name, phone_number = raw_data.split(" : ")

    if phone_number.isnumeric():
        phonebook[name] = phone_number
    else:
        phonebook[phone_number] = name

    raw_data = input()

for key in sorted(phonebook):
    print(f'{key} -> {phonebook[key]}')
