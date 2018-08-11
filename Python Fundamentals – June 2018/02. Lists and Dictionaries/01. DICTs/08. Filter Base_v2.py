raw_data = input()
age = {}
salary = {}
position = {}


def is_int(n):
    try:
        float_n = float(n)
        int_n = int(float_n)
    except ValueError:
        return False
    else:
        return float_n == int_n


def is_float(n):
    try:
        float_n = float(n)
    except ValueError:
        return False
    else:
        return True


while raw_data != 'filter base':

    name, user_info = raw_data.split(' -> ')

    if is_int(user_info):
        age[name] = int(float(user_info))

    elif is_float(user_info):
        salary[name] = float(user_info)

    else:
        position[name] = user_info

    raw_data = input()

filter_by = input()

if filter_by == 'Salary':
    for name in salary:
        print(f'Name: {name}')
        print(f'{"Salary"}: {salary[name]}')
        print("=" * 20)
elif filter_by == 'Position':
    for name in position:
        print(f'Name: {name}')
        print(f'{"Position"}: {position[name]}')
        print("=" * 20)
else:
    for name in age:
        print(f'Name: {name}')
        print(f'{"Age"}: {age[name]}')
        print("=" * 20)
