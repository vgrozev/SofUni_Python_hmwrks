import sqlite3


def main():
    with sqlite3.connect('data/sales-example.db') as connection:
        print_catalog(connection)
        # demo_sql_injection(connection)
        new_catalog_entry(connection, item_key='11111111', category='LJLJLJLH')
        print_catalog(connection)


def demo_sql_injection(conection):
    """
    !!!!!!  DO NOT DO THIS !!!!!!!!!!!!!

    :param conection:
    :return:
    """

    print('DEMO: SQL Injections')

    username = input("username = ")
    ### username = boris' or 1=1; --
    password = 'asdfasfa232423424234234sdfsfsfsfsdsf'
    wrong_sql = "select * from users where username = '{}' and password = '{}';".format(username, password)
    print(wrong_sql)

    # item_key = input("item_id = ")
    ### item_id = 3456'); --
    category = "asdfadfasdf"
    # wrong_sql = "insert into catalog (item_key, category) values ('{}', '{}')".format(item_key, category)
    # print(wrong_sql)


def new_catalog_entry(connection, item_key: str, category: str):
    cursor = connection.cursor()
    cursor.execute(
        'insert into catalog (item_key, category) values (?, ?)',
        [item_key, category]
    )


def print_catalog(connection):
    cursor = connection.cursor()
    cursor.execute('select * from catalog')
    # for row in cursor.fetchall():
    #     print("Record")
    #     print("\t{}".format(row[0]))
    #     print("\t{}".format(row[1]))
    #     print("\t{}".format(row[2]))

    for row_number, row in enumerate(cursor.fetchall(), start=1):
        print("\nRecord #{}".format(row_number))
        print("\tid = {}".format(row[0]))
        print("\titem_key = {}".format(row[1]))
        print("\tcategory = {}".format(row[2]))


if __name__ == '__main__':
    main()
