raw_data = input()

employee = {}


def is_float(n):
    try:
        float_n = float(n)
    except ValueError:
        return False
    else:
        return True


while raw_data != 'filter base':

    name, user_info = raw_data.split(' -> ')

    if name not in employee:
        employee[name] = {}

    if user_info.isnumeric():
        employee[name]['Age'] = int(user_info)

    elif is_float(user_info):
        employee[name]['Salary'] = float(user_info)

    else:
        employee[name]['Position'] = user_info

    raw_data = input()

filter_by = input()

# for key in employee:
#     print(f"{key} -> {employee[key]}")


for name in employee:
    if filter_by in employee[name]:
        print(f'Name: {name}')
        print(f'{filter_by}: {employee[name][filter_by]}')
        print("=" * 20)
