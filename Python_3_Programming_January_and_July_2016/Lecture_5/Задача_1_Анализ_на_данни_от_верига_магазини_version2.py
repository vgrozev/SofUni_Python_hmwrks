# -*- coding: UTF-8 -*-

"""
1. Load the catalog file
2. Load the sales file
...
"""

from datetime import timezone

from pprint import pprint

from Python_3_Programming_January_and_July_2016.Lecture_5.catalog import load_catalog
from Python_3_Programming_January_and_July_2016.Lecture_5.sales import load_sales, KEY_PRICE, KEY_TS, KEY_ITEM_ID, \
    KEY_CITY

import time

from Python_3_Programming_January_and_July_2016.Lecture_5.sales import load_sales, KEY_PRICE, KEY_TS, KEY_ITEM_ID, KEY_CITY

import time

start_time = time.time()

CATALOG = 'sales-analysis-assignment-all/catalog.csv'
SALES_1M = 'sales-analysis-assignment-all/sales-1M.csv'
SALES_10K = "sales-analysis-assignment-all/sales-10K.csv"
SALES_100K = 'sales-analysis-assignment-all/sales-100K.csv'


def main():
    catalog = load_catalog(CATALOG)
    sales = load_sales(SALES_10K)
    # sales = load_sales(SALES_100K)
    # sales = load_sales(SALES_1M)
    # sales = load_sales(SALES_10K)
    # sales = load_sales(SALES_100K)
    sales = load_sales(SALES_1M)

    print_total_stats(sales)
    print_top_by_category(sales, catalog)
    print_top_by_city(sales)
    print_top_by_hour(sales)

    # pprint(sales[:10])

    print("--- %s seconds ---" % (time.time() - start_time))


def print_total_stats(sales):
    """

    """
    total_amount = 0
    total_count = len(sales)

    min_timestamp = None
    max_timestamp = None

    for sale in sales:  # see sales.load_sales() for details
        total_amount += sale[KEY_PRICE]
        ts = sale[KEY_TS]

        if min_timestamp is None or ts < min_timestamp:
            min_timestamp = ts
        if max_timestamp is None or ts > max_timestamp:
            max_timestamp = ts

            # min(sale['ts'] for sale in sales)
            # max(sale['ts'] for sale in sales)

            # if total_count > 0:
            #     average_price = total_amount / total_count
            # else:
            #     average_price = None

    print("""
Обобщение
---------
    Общ брой продажби: {total_count}
    Общо сума продажби: {total_amount:.2f} €
    Средна цена на продажба: {average_price:.2f} €
    Начало на период на данните: {min_ts}
    Край на период на данните: {max_ts}
""".format(
        total_count=total_count,
        total_amount=total_amount,
        average_price=total_amount / total_count if total_count else None,
        min_ts=min_timestamp,
        max_ts=max_timestamp,
    ))


def print_top_by_category(sales, catalog):
    """

    """

    amounts_by_category = {}  # key: category name, value: accumulated sum of sales

    for sale in sales:
        item_id = sale[KEY_ITEM_ID]
        price = sale[KEY_PRICE]
        category_name = catalog.get(item_id, None)

        if category_name not in amounts_by_category:
            amounts_by_category[category_name] = 0

        amounts_by_category[category_name] += price

    amounts_by_category_sorted = []
    for category_name, total_amount in amounts_by_category.items():
        amounts_by_category_sorted.append((total_amount, category_name))

    amounts_by_category_sorted.sort(reverse=True)

    print("""
Сума на продажби по категории (top 5)
-----------------------------
    """)
    for total_amount, category_name in amounts_by_category_sorted[:5]:
        print("     {}: {:.2f} €".format(category_name, total_amount))


def print_top_by_city(sales):
    """

    """

    amounts_by_city = {}  # key: city name, value: accumulated sum of sales
    for sale in sales:
        city_name = sale[KEY_CITY]
        price = sale[KEY_PRICE]

        if city_name not in amounts_by_city:
            amounts_by_city[city_name] = 0

        amounts_by_city[city_name] += price

    amounts_by_city_sorted = []
    for city_name, total_amount in amounts_by_city.items():
        amounts_by_city_sorted.append((total_amount, city_name))

    amounts_by_city_sorted.sort(reverse=True)

    print("""
Сума на продажби по градове (top 5)
-----------------------------
    """)
    for total_amount, city_name in amounts_by_city_sorted[:5]:
        print("     {}: {:.2f} €".format(city_name, total_amount))


def print_top_by_hour(sales):
    """

    """
    amounts_by_ts = {}  # key: city name, value: accumulated sum of sales
    for sale in sales:
        ts = sale[KEY_TS].replace(minute=0, second=0).astimezone(timezone.utc)
        price = sale[KEY_PRICE]

        if ts not in amounts_by_ts:
            amounts_by_ts[ts] = 0

        amounts_by_ts[ts] += price

    amounts_by_ts_sorted = []
    for ts, total_amount in amounts_by_ts.items():
        amounts_by_ts_sorted.append((total_amount, ts))

    amounts_by_ts_sorted.sort(reverse=True)

    print("""
Сума на продажби по час (top 5)
-----------------------------
    """)
    for total_amount, ts in amounts_by_ts_sorted[:5]:
        print("     {}: {:.2f} €".format(ts, total_amount))


if __name__ == '__main__':
    main()
