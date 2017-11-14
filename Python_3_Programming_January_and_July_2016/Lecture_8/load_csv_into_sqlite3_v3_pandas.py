"""
    Като използвате кода от задачата в предишната лекция - Анализ на данни от верига магазини,
    импортирайте данните ж SQLlite база данни.
    Използвайте модулите от предишните лекции, съдържащи CatalogEntry & Sale
"""

import pandas as pd
import sqlite3
import sqlalchemy

# DB_FILENAME = 'data/sales-1M.db'
# DB_FILENAME = 'data/sales-10K.db'
DB_FILENAME = 'data/sales-100K.db'

# SALES_FILENAME = 'csv_files/sales-1M.csv'
# SALES_FILENAME = 'csv_files/sales-10K.csv'
SALES_FILENAME = 'csv_files/sales-100K.csv'

CATALOG_FILENAME = 'csv_files/catalog.csv'


def main():
    with sqlite3.connect(DB_FILENAME, isolation_level=None) as connection:

        print("Connection opened")

        cursor = connection.cursor()
        engine = sqlalchemy.create_engine('sqlite:///' + DB_FILENAME)

        create_tables(cursor)
        print("Tables created")

        import_catalog_into_db(engine, CATALOG_FILENAME)
        print("Catalog imported")

        import_sales_into_db(engine, SALES_FILENAME)
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


def import_catalog_into_db(engine, catalog_file_name):
    df = pd.read_csv(catalog_file_name, names=['item_key', 'category'])
    df.to_sql('catalog', engine, if_exists='append', index=False)


def import_sales_into_db(engine, sales_file_name):
    df = pd.read_csv(sales_file_name, names=['item_id', 'country', 'city_name', 'sale_timestamp', 'price'])
    df.to_sql('sale', engine, if_exists='append', index=False)


if __name__ == '__main__':
    main()