n = int(input())

stars_patern = "*" * (n - 2)
dash_patern = "-" * (n - 2)
upper_mid_section = "\ /"
lower_mid_section = "/ \\"
central_section = " " * (n - 1) + "@" + " " * (n - 1)
half_way = (2 * (n - 2) + 1)//2

for i in range(1, half_way + 1):
    if i % 2 != 0:
        print(stars_patern + upper_mid_section + stars_patern)
    else:
        print(dash_patern + upper_mid_section + dash_patern)

print(central_section)


for j in range(1, half_way + 1):
    if j % 2 != 0:
        print(stars_patern + lower_mid_section + stars_patern)
    else:
        print(dash_patern + lower_mid_section + dash_patern)



