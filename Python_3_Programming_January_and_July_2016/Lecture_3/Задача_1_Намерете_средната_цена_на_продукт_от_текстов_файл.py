FILENAME_1 = 'catalog_sample.csv'
FILENAME_2 = 'catalog_full.csv'

with open(FILENAME_1, 'r', encoding='utf-8') as catalog:
    count = 0
    suma = 0
    for line in catalog:
        line = line.split(',')
        count += 1
        suma += float(line[-1])
average = suma/count
print("The average price from the 'sample' file is: ", round(average, 2))

with open(FILENAME_2, 'r', encoding='utf-8') as catalog:
    all_prices = list()
    for line in catalog:
        line = line.split(',')
        all_prices.append(float(line[-1]))
print(len(all_prices))
print("The average price from the 'full' file is: ", round(sum(all_prices)/len(all_prices), 2))


# average from all files
files = [FILENAME_1, FILENAME_2]
with open('combined.csv', 'w', encoding='utf-8') as concat_file:
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            concat_file.write(f.read())
with open('combined.csv', 'r', encoding='utf-8') as catalog:
    all_prices = list()
    for line in catalog:
        line = line.split(',')
        all_prices.append(float(line[-1]))
print("The average price from all files is: ", round(sum(all_prices)/len(all_prices), 2))


