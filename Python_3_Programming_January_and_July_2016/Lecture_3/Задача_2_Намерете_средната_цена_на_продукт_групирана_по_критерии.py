FILENAME = 'catalog_full.csv'
# FILENAME = 'catalog_sample.csv'

gender_price_tuple_list = list()

with open(FILENAME, 'r', encoding='utf-8') as catalog:
    for line in catalog:
        line = line.split(',')
        # produces a list of gender/age , price tuples
        gender_price_tuple_list.append((line[5], line[6].strip()))

unique_gen = set(gender[0] for gender in gender_price_tuple_list)
print("\nThe set of unique age groups is: {}\n".format(unique_gen))

print("=========================================\n")

for age_group in unique_gen:
    gen_sum_list = list()
    for gen_price_tuple in gender_price_tuple_list:
        if gen_price_tuple[0] == age_group:
            gen_sum_list.append(float(gen_price_tuple[1]))
    avg = round(sum(gen_sum_list) / len(gen_sum_list), 2)
    print("The average price for age group \"{}\" is: ${} ".format(age_group, avg))


# --- не работи коректно, защото му трябва начин да брои на колко да раздели във всеки тюпъл ---- №
# sums = [(gend, round(sum(float(gender[1]) / index for index, gender in enumerate(gender_price, start=1) if gender[0] == gend), 2)) for gend in unique_gen]
# print(*sums, sep='\n')
# print('\n'.join(str(p) for p in sums))
# for p in sums:
#     print('The average price grouped by gender is: {} --> ${}'.format(*p))
