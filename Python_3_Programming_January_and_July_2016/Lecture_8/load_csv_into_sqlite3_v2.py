"""
    Като използвате кода от задачата в предишната лекция - Анализ на данни от верига магазини,
    импортирайте данните ж SQLlite база данни.
    Използвайте модулите от предишните лекции, съдържащи CatalogEntry & Sale
"""

import sqlite3
import csv
import iso8601

# DB_FILENAME = 'data/sales-1M.db'
DB_FILENAME = 'data/sales-10K.db'
# DB_FILENAME = 'data/sales-100K.db'

# SALES_FILENAME = 'csv_files/sales-1M.csv'
SALES_FILENAME = 'csv_files/sales-10K.csv'
# SALES_FILENAME = 'csv_files/sales-100K.csv'

CATALOG_FILENAME = 'csv_files/catalog.csv'

COLUMN_ITEM_ID = 0
COLUMN_COUNTRY = 1
COLUMN_CITY = 2
COLUMN_TS = 3
COLUMN_PRICE = 4
COLUMN_CATEGORY = 5

# KEY_ITEM_ID = 'item_id'
# KEY_COUNTRY = 'country'
# KEY_CITY = 'city'
# KEY_TS = 'ts'
# KEY_PRICE = 'price'



def main():
    with sqlite3.connect(DB_FILENAME, isolation_level=None) as connection:

        cursor = connection.cursor()
        print("Connection opened")

        create_tables(cursor)
        print("Tables created")

        import_catalog_into_db(cursor, CATALOG_FILENAME)
        print("Catalog imported")

        import_sales_into_db(cursor, SALES_FILENAME)
        print("Sales imported")


def create_tables(cursor):

    cursor.execute("drop table if exists sale;")
    cursor.execute("drop table if exists catalog;")

    cursor.execute("""
        create table if not exists sale (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_id varchar(200) NOT NULL,
            country varchar(3),
            city_name varchar(60), 
            sale_timestamp TEXT,
            price NUMERIC
        );
    """)

    cursor.execute("""
        create table if not exists catalog (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_key varchar(200),
            category varchar(200)
        );
    """)


def import_catalog_into_db(cursor, catalog_file_name):

    with open(catalog_file_name, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            item_id = row[COLUMN_ITEM_ID]
            category = row[COLUMN_CATEGORY]

            cursor.execute(
                'insert into catalog (item_key, category) values (?, ?)',
                [item_id, category]
            )


def import_sales_into_db(cursor, sales_file_name):

    with open(sales_file_name, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            sale_timestamp = iso8601.parse_date(row[COLUMN_TS])

            cursor.execute(
                'insert into sale (item_id, country, city_name, sale_timestamp, price) values (?, ?, ?, ?, ?)',
                [
                    row[COLUMN_ITEM_ID],
                    row[COLUMN_COUNTRY],
                    row[COLUMN_CITY],
                    sale_timestamp.isoformat(),
                    float(row[COLUMN_PRICE])
                ]
            )

if __name__ == '__main__':
    main()
