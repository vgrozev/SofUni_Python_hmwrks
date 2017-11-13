#!/usr/bin/env python3 -tt

import os
import sys
import sqlite3

from Python_3_Programming_January_and_July_2016.Lecture_8.sales import load_sale_data
from Python_3_Programming_January_and_July_2016.Lecture_8.catalog import load_catalog_by_item_id


def main():

    try:
        file_catalog, file_sales, db_filename = _parse_cmd_line_arg()

        sales = load_sale_data(file_sales)
        catalog_by_item_id = load_catalog_by_item_id(file_catalog)

        with sqlite3.connect(db_filename, isolation_level=None) as connection:
            cursor = connection.cursor()
            cursor.execute("pragma foreign_keys=on;")

            print("Connection opened")
            create_tables(connection)
            print("Tables created")
            import_catalog_into_db(catalog_by_item_id, connection)
            print("Catalog imported")
            import_sales_into_db(sales, connection)
            print("Sales imported")

        return 0
    except Exception as e:
        print("Error: " + str(e))
        return 1


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute("""
        drop table if exists sale;
    """)

    cursor.execute("""
        drop table if exists catalog;
    """)

    cursor.execute("""
        create table if not exists catalog (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_id varchar(200) UNIQUE,
            name varchar(200),
            colors varchar(200),
            group_name varchar(200),
            sport_type varchar(200),
            category varchar(200),
            subcategory varchar(200),
            age_type varchar(200)
        );
    """)

    cursor.execute("""
        create table if not exists sale (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            catalog_id INTEGER NOT NULL,
            country varchar(3),
            city varchar(60),
            sale_timestamp TEXT,
            price NUMERIC,
            FOREIGN KEY(catalog_id) REFERENCES catalog(id)
        );
    """)



def import_catalog_into_db(catalog_by_item_id, connection):
    cursor = connection.cursor()
    for catalog_entry in catalog_by_item_id.values():
        cursor.execute(
            """insert into catalog
                (item_id, name, colors, group_name, sport_type, category, subcategory, age_type)
            values
                (?, ?, ?, ?, ?, ?, ?, ?)
                """,
            [
                catalog_entry.item_id,
                catalog_entry.name,
                catalog_entry.colors,
                catalog_entry.group,
                catalog_entry.sport_type,
                catalog_entry.category,
                catalog_entry.subcategory,
                catalog_entry.age_type
            ]
        )


def import_sales_into_db(sales, connection):
    cursor = connection.cursor()

    inserted_rows = 0

    for sale in sales:
        # TODO: implement
        cursor.execute('select id from catalog where item_id = ?', [sale.item_id])
        result = cursor.fetchone()
        if result:
            catalog_id = result[0]
            cursor.execute(
                """insert into sale
                    (catalog_id, country, city, sale_timestamp, price)
                values
                    (?, ?, ?, ?, ?)
                    """,
                [
                    catalog_id,
                    sale.country,
                    sale.city,
                    sale.sale_timestamp.isoformat(),
                    str(sale.price)
                ]
            )
        else:
            print("No catalog item found for item id: {}".format(sale.item_id))

        inserted_rows += 1
        if inserted_rows % 200 == 0:
            print(".", end='', flush=True)
    print('.')


def _parse_cmd_line_arg():

    if len(sys.argv) != 4:
        raise ValueError("Usage: {} catalogue.csv sale-report.csv output.db".format(sys.argv[0]))

    file_catalog = sys.argv[1]
    file_sales = sys.argv[2]
    db_filename = sys.argv[3]

    if not os.access(file_catalog, os.R_OK) or not os.path.isfile(file_catalog):
        raise ValueError("File {} does not exits or not readable".format(file_catalog))

    if not os.access(file_sales, os.R_OK) or not os.path.isfile(file_sales):
        raise ValueError("File {} does not exits or not readable".format(file_sales))

    # if not os.access(db_filename, os.R_OK) or not os.path.isfile(file_catalog):
    #     raise ValueError("File {} does not exits or not readable".format(db_filename))

    result = file_catalog, file_sales, db_filename
    return result


if __name__ == "__main__":
    sys.exit(main())