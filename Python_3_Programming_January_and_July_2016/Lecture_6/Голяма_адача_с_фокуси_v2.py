# -*- coding: UTF-8 -*-

import csv
import iso8601
import time
from datetime import timezone

COLUMN_ITEM_ID = 0
COLUMN_COUNTRY = 1
COLUMN_CITY = 2
COLUMN_TS = 3
COLUMN_PRICE = 4
COLUMN_CATEGORY = 5

KEY_ITEM_ID = 'item_id'
KEY_COUNTRY = 'country'
KEY_CITY = 'city'
KEY_TS = 'ts'
KEY_PRICE = 'price'

start_time = time.time()

CATALOG = 'sales-analysis-assignment-all/catalog.csv'
SALES_1M = 'sales-analysis-assignment-all/sales-1M.csv'
SALES_10K = "sales-analysis-assignment-all/sales-10K.csv"
SALES_100K = 'sales-analysis-assignment-all/sales-100K.csv'


def main():
    catalog = load_catalog(CATALOG)

    # sales = SALES_10K
    # sales = SALES_100K
    sales = SALES_1M

    print("Analysys")

    total_amount = 0
    total_count = 0
    min_timestamp = None
    max_timestamp = None
    amounts_by_category = {}  # key: category name, value: accumulated sum of sales
    amounts_by_city = {}  # key: city name, value: accumulated sum of sales
    amounts_by_ts = {}  # key: city name, value: accumulated sum of sales by hour

    total_stats_string = """
Обобщение
---------
    Общ брой продажби: {total_count}
    Общо сума продажби: {total_amount:.2f} €
    Средна цена на продажба: {average_price:.2f} €
    Начало на период на данните: {min_ts}
    Край на период на данните: {max_ts}
"""

    category_string = """
    Сума на продажби по категории (top 5)
-----------------------------
"""
    city_string = """
    Сума на продажби по градове (top 5)
-----------------------------
"""
    hours_string = """
    Сума на продажби по час (top 5)
-----------------------------
"""

    for sale in load_sales(sales):
        total_amount += sale[KEY_PRICE]
        total_count += 1
        ts = sale[KEY_TS]

        if min_timestamp is None or ts < min_timestamp:
            min_timestamp = ts
        if max_timestamp is None or ts > max_timestamp:
            max_timestamp = ts

        # calculate top by category #####################################################
        calculate_top(catalog.get(sale[KEY_ITEM_ID], None), sale[KEY_PRICE], amounts_by_category)

        # calculate top by city #########################################################
        calculate_top(sale[KEY_CITY], sale[KEY_PRICE], amounts_by_city)

        # calculate top by hour #########################################################
        calculate_top(sale[KEY_TS].replace(minute=0, second=0).astimezone(timezone.utc), sale[KEY_PRICE], amounts_by_ts)

    print_total_stats(total_count, total_amount, min_timestamp, max_timestamp, total_stats_string)
    print_top(amounts_by_category, category_string)
    print_top(amounts_by_city, city_string)
    print_top(amounts_by_ts, hours_string)

    ##############################################################################
    # This is to measure the time to run for the program
    print("\nTime to run: \n--- %s seconds ---" % (time.time() - start_time))


def calculate_top(name, price, amounts_dict):
    gen_price = price
    gen_name = name
    amounts = amounts_dict

    if gen_name not in amounts:
        amounts[gen_name] = 0

    amounts[gen_name] += gen_price
    return amounts


def print_total_stats(total_c, total_a, min_time, max_time, str_to_print: str):
    print(str_to_print.format(
        total_count=total_c,
        total_amount=total_a,
        average_price=total_a / total_c if total_c else None,
        min_ts=min_time,
        max_ts=max_time, ))


def print_top(dict_of_amounts: dict, str_to_print: str):
    dict_of_amounts_sorted = list(dict_of_amounts.items())
    dict_of_amounts_sorted.sort(key=lambda k_value: k_value[1], reverse=True)
    print(str_to_print)
    for name, total_amount in dict_of_amounts_sorted[:5]:
        print("     {}: {:.2f} €".format(name, total_amount))


def load_catalog(filename: str) -> dict:
    result = {}
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            item_id = row[COLUMN_ITEM_ID]
            category = row[COLUMN_CATEGORY]
            result[item_id] = category
    return result


def load_sales(filename: str) -> list:
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            sale = {KEY_ITEM_ID: row[COLUMN_ITEM_ID],
                    KEY_COUNTRY: row[COLUMN_COUNTRY],
                    KEY_CITY: row[COLUMN_CITY],
                    KEY_TS: iso8601.parse_date(row[COLUMN_TS]),
                    KEY_PRICE: float(row[COLUMN_PRICE])
                    }
            yield sale


if __name__ == '__main__':
    main()
