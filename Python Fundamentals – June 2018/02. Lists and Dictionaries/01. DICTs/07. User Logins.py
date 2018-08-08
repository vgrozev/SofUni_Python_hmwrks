raw_data = input()

username_password = {}
unsuccessful_logins = 0

while raw_data != 'login':

    user, password = raw_data.split(' -> ')

    username_password[user] = password

    raw_data = input()

raw_data = input()
while raw_data != 'end':

    user, password = raw_data.split(' -> ')

    if username_password.get(user) == password:
        print(f'{user}: logged in successfully')
    else:
        print(f'{user}: login failed')
        unsuccessful_logins += 1

    raw_data = input()

print("unsuccessful login attempts:", unsuccessful_logins)
