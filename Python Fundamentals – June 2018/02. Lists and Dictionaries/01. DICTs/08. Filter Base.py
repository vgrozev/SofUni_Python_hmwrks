raw_data = input()

employee = {}


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

    if name not in employee:
        employee[name] = {}

    if user_info.isnumeric():
            if user_info.isdigit():
                employee[name]['Age'] = int(user_info)

            else:
                employee[name]['Salary'] = float(user_info)
    else:
        employee[name]['Position'] = user_info

    raw_data = input()

filter_by = input()

# for key in employee:
#     print(f"{key} -> {employee[key]}")


for name in sorted(employee, reverse=True):
    if filter_by in employee[name]:
        print(f'Name: {name}')
        print(f'{filter_by}: {employee[name][filter_by]}')
        print("=" * 20)
