raw_data = input()

shells = {}

while raw_data != "Aggregate":

    region, shell_size = raw_data.split()

    if region not in shells:
        shells[region] = []
    if int(shell_size) not in shells[region]:
        shells[region].append(int(shell_size))

    raw_data = input()

for key in shells:
    giand_shell = sum(shells[key]) - int((sum(shells[key]) / len(shells[key])))
    print(f'{key} -> ', end='')
    print(*shells[key], sep=', ', end='')
    print(f' ({giand_shell})')

