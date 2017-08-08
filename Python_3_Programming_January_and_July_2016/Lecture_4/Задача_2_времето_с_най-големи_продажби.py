"""
    Вие сте собственик на online магазин, и искате да проверите в кои дни и часове има най-много продажби. Най-много продажби означава сумата на тези продажби, не броят на извършените продажби.
    Свалете файла sales.csv, който съдържа 1000 продажби. Файлът е CSV като първата колона е датата и часа на продажбата, втората колона е сумата на продажбата. Файлът не е подреден.
    Напишете код, който показва в кой ден е имало най-много продажби като сума от всички продажби за този ден.
    
    Пример: В понеделник е имало продажби за 2000 лева, във вторник за 2345 лева, а в сряда за 897 лева. Денят с най-много продажби е вторник.
    
    Разширение на задачата
    Разширете кода си, така че да показва в кой час има най-много продажби. Интересува ни часа, а не деня.
    Пример: За целия период между 13:00 и 14:00 е имало продажби за 897 лева, между 14:00 и 15:00 е имало продажби за 456 лева. Между 13:00 и 14:00 е имало повече продажби отколкото между 14:00 и 15:00
---------------------------------------------------------------
date-time strip example:

date_string2 = '2016-07-26 21:38:23.770340'
datetime_object2 = iso8601.parse_date(date_string2)
dt_group_by2 = datetime_object2.replace(minute=0, second=0, microsecond=0)
print(dt_group_by2)
"""
import iso8601 as time_m

FILENAME = 'sales.csv'
day_sale_dict = dict()

# variation 1 --> dates
with open(FILENAME, 'r', encoding='utf-8') as catalog:
    for line in catalog:
        line = line.rstrip().split(',')
        key, value = line
        key = time_m.parse_date(key).replace(hour=0, minute=0, second=0, microsecond=0)
        if key not in day_sale_dict:
            day_sale_dict[key] = float(value)
        else:
            day_sale_dict[key] = float(value) + day_sale_dict[key]

    for k, v in day_sale_dict.items():
        k = str(k).split()
        print(k[0], '-->', round(v, 2))

    print('\n')
    key_with_max = max(day_sale_dict, key=day_sale_dict.get)
    print(str(key_with_max).split()[0], 'is the day with MAX sales :', round(day_sale_dict[key_with_max], 2))

# variation 1 -->
day_sale_dict2 = dict()
with open(FILENAME, 'r', encoding='utf-8') as catalog:
    for line in catalog:
        line = line.rstrip().split(',')
        key, value = line
        key = time_m.parse_date(key).hour
        if key not in day_sale_dict2:
            day_sale_dict2[key] = float(value)
        else:
            day_sale_dict2[key] = float(value) + day_sale_dict2[key]

    print('\n')
    for k, v in day_sale_dict2.items():
        print(k, '-->', round(v, 2))

    key_with_max = max(day_sale_dict2, key=day_sale_dict2.get)
    print('\n')
    print(str(key_with_max).split()[0], 'is the HOUR with MAX sales :', round(day_sale_dict2[key_with_max], 2))
