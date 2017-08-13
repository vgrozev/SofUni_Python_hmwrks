"""
Разполагаме с каталог на стоки и данни за продажби на голям производител на спортни стоки,
и трябва да направим анализ на тази информация.
Крайната цел на задачата е да анализираме данните и да визуализираме:

    $ python3    analyze.py   catalog.csv   sales-10K.csv
    
    Обобщение
    ---------
        Общ брой продажби: 10000
        Общо сума продажби: 3191507.82 €
        Средна цена на продажба: 319.15 €
        Начало на период на данните: 2015-12-01T08:00:48+01:00
        Край на период на данните: 2016-01-24T20:49:38+00:00
    
    Сума на продажби по категории (top 5)
    -----------------------------
        SHOES: 1519077.15 €
        T-SHIRTS: 207615.78 €
        HEADWEAR: 176304.77 €
        BALLS: 146092.19 €
        JACKETS: 130226.14 €
    
    Сума на продажби по градове (top 5)
    -----------------------------
        Manchester: 100620.74 €
        Liverpool: 96607.68 €
        London: 92239.71 €
        Nottingham: 90084.01 €
        Glasgow: 87052.21 €
    
    Сума на продажби по час (top 5)
    -----------------------------
        2015-12-01 12:00:00+01:00: 9209.70 €
        2016-01-17 10:00:00+02:00: 8811.59 €
        2016-01-05 20:00:00+01:00: 8590.52 €
        2015-12-29 20:00:00+02:00: 8270.59 €
        2016-01-05 10:00:00+01:00: 8028.91 €
        
    Обърнете внимание, че часът от последния анализ трябва да бъде в UTC часова зона - "+00:00".
----------------

Входни данни и описание на формат на данните

    Продуктов каталог - файл 'catalog.csv'
    Файловете с продуктовия каталог са във формат CSV (UTF-8), и съдържа следните колони:
    
        Идентификационен номер на артикула;
        Наименование на артикула;
        Цветове, в които артикулът е наличен;
        Група на артикула;
        Спорт, за който е предназначен артикулът;
        Категория
        Подкатегория
        Пол, за който е предназначен артикула - мъже, жени, unisex, деца, бебета
        
    Примерни редове от файла с каталога:
    
        "538352","TYGUN II","BLACK/RUNNINWHT","FOOTWEAR","BOXING","SHOES","SHOES (LOW)","Men"
        "42259","M TEAM TEE","WHITE/DARKNAVY","TEXTILES","TENNIS","T-SHIRTS","T-SHIRT (SHORT SLEEVE)","Men"
        "562319","NOVA WALK 06","DARONX/METSIL/DSHALE","FOOTWEAR","WALKING","SHOES","SHOES (LOW)","Men"
        "G13130","COMPOUND","BLACK1/BLACK1/LGTIPD","FOOTWEAR","GOLF","SHOES","SHOES (LOW)","Men"
        "396559","+TG SWERVE DBMI","WHITE/BLACK","HARDWARE","FOOTBALL/SOCCER","BALLS","BALL (MACHINE-STITCHED)","Men"
        "34549","LTA SS2G C","RUNWHI/SHABLU/VAPOUR","FOOTWEAR","BASKETBALL","SHOES","SHOES (LOW)","Kid"

--------------

Данни за продажби - файлове 'sales-*.csv'

Файловете с продажби са във формат CSV (UTF-8), и съдържат следните колони:

    Идентификационен номер на артикула;
        Държава, в която е била извършена продажбата (ISO code)
        Име на град, в която е била извършена продажбата;
        Дата/час на продажбата с timezone, във формат ISO8601;
        Цена на продажбата (цените на един и същ артикул в различните държави са различни)
        
Примерни редове от файл с продажби:

    "561712","ES","Murcia","2015-12-11T17:14:05+01:00",43.21
    "K81938","FR","Nantes","2016-01-14T20:58:38+01:00",36.57
    "41975","IT","Catania","2016-01-12T10:57:50+01:00",409.58
    "538352","DE","Düsseldorf","2015-12-18T20:50:21+01:00",95.03

==============
    
Насоки
    Parse на дати в ISO8601 формат
        За да parse-нете датите във файловете с продажби, използвайте модула iso8601
        
        import iso8601
        ...
        dt = iso8601.parse_date('2015-12-11T17:14:05+01:00')
        print(dt)
        2015-12-11 17:14:05+01:00
        
    Работа с datetimes, които съдържат информация за часови зони
        Вземане на текуща дата/час в часова зона UTC
        
        from datetime import datetime, timezone
        
        now_utc = datetime.now(tz=timezone.utc)
        print(now_utc)
        '2016-01-26 14:38:02.720755+00:00'
        
    Конвертиране към от друга часова зона към UTC
        from datetime import datetime, timezone
        import iso8601
        
        d = iso8601.parse_date('2015-12-18T20:50:21+01:00')
        print(d)
        '2015-12-18 20:50:21+01:00'
        
        d_in_utc = d.astimezone(timezone.utc)
        print(d_in_utc)
        '2015-12-18 19:50:21+00:00'

"""
from datetime import datetime, timezone
import iso8601 as iso_time
import csv
import pprint
from collections import defaultdict
from progressbar import ProgressBar

pbar = ProgressBar()  # just a progressbar --> not essential for the solution

CATALOG = 'sales-analysis-assignment-all/catalog.csv'
SALES_1M = 'sales-analysis-assignment-all/sales-1M.csv'
SALES_10K = "sales-analysis-assignment-all/sales-10K.csv"
SALES_100K = 'sales-analysis-assignment-all/sales-100K.csv'

headers = ['id', 'country', 'town', 'date']
COUNT = 0


#########################################################
# Organize data in a nested dict
#########################################################
def sort_sales(sales_file) -> dict:
    final_sales_dict = defaultdict(dict)

    with open(sales_file, 'r', newline='', encoding='utf-8') as sales:
        reader = csv.reader(sales)
        for row in pbar(reader):  # every line of the file as a list  (pbar() is a progress bar )

            global COUNT
            COUNT += 1
            row[-1] = float(row[-1])  # convert the price to float
            # leave only hours and convert it back to string:
            row[-2] = str(iso_time.parse_date(row[-2]).replace(minute=0, second=0))

            for i, column in enumerate(row[:-1]):  # loop trough the list excluding the last element, which is 'price'
                if column in final_sales_dict.get(headers[i], {}):
                    # if the key for the inner dictionary already exist, sum prices:
                    value = final_sales_dict[headers[i]][column] + row[-1]
                else:
                    value = row[-1]

                # add resulting price as value to a key/pair in the inner dict
                final_sales_dict[headers[i]][column] = round(value, 2)

    return final_sales_dict


#########################################################
# Total values of nested dicts
#########################################################
def sum_total(dict_to_sum: dict) -> float:
    for sub_dict in dict_to_sum.items():
        values = [v for v in sub_dict[1].values()]  # create a list of the second values of the tuple 'sub_dict'

    return round(sum(values), 2)


#########################################################
# list top 5 of provided criteria
#########################################################
def top_five(criteria: str, data_dict) -> list:
    data_price_tuples = [(price, data) for data, price in data_dict[criteria].items()]
    data_price_tuples.sort(reverse=True)
    top_5_list = [(t[1], t[0]) for t in data_price_tuples[:5]]  #reverse them so the town is first
    print(top_5_list)
    return top_5_list

def convert_to_UTC(data_dict) -> dict:


    return ""

sorted_sales_dict = sort_sales(SALES_10K)
# pprint.pprint(sorted_sales_dict)  # pretty print for nested dictionaries
total = sum_total(sorted_sales_dict)
average = round(total / COUNT, 2)
top_5_towns = top_five(headers[2], sorted_sales_dict)


top_5_dates = top_five(headers[3], sorted_sales_dict)

print('Обобщение')
print('---------')
print('    Общ брой продажби: ', COUNT)
print('    Общо сума продажби: {}'.format(total), '\u20ac')
print('    Средна цена на продажба: {}'.format(average), '\u20ac')
print("===========  temp ===========")
print('Сума на продажби по градове (top 5)')
print('-----------------------------')
# convert the tuples to strings and print them separate lines with a ure sign at the end of each
print(''.join(["    %s: %s \u20ac \n" % tup for tup in top_5_towns]))
print("===========  temp ===========")
print('Сума на продажби по час (top 5)')
print('-----------------------------')
# convert the tuples to strings and print them separate lines with a ure sign at the end of each
print(''.join(["    %s: %s \u20ac \n" % tup for tup in top_5_dates]))
