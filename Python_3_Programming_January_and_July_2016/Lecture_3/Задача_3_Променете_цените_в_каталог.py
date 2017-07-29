FILE_IN = 'catalog_full.csv'
FILE_OUT = 'catalog_plus_75.csv'
PRICE = -1    # currently at the last position --> index -1
PERCENT_INCREASE = 0.75   # 75% = 75/100 = 0.75

with open(FILE_IN, 'r', encoding='utf-8') as catalog:
    with open(FILE_OUT, 'w', encoding='utf-8') as catalog_plus_75:
        for line in catalog:
            line = line.split(',')
            old_price = float(line[PRICE])
            new_price = round((old_price * PERCENT_INCREASE) + old_price, 2)
            line[PRICE] = str(new_price)
            catalog_plus_75.write(','.join(line) + '\n')
