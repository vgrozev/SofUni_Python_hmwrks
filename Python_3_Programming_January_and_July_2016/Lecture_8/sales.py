import csv
import iso8601
from datetime import datetime, timezone
from decimal import Decimal


class Item(object):

    def __init__(self, item_id, country, city, sale_timestamp, price):
        self.item_id = str(item_id)
        self.country = str(country)
        self.city = str(city)

        if not isinstance(sale_timestamp, datetime):
            self.sale_timestamp = iso8601.parse_date(str(sale_timestamp))
        else:
            self.sale_timestamp = sale_timestamp

        if self.sale_timestamp.tzinfo is None:
            raise ValueError("Error: Naive datetime is not supported")
        else:
            self.sale_timestamp = self.sale_timestamp.astimezone(timezone.utc)

        self.price = Decimal(price)

    def __repr__(self):
        return "Item: " + str(self.__dict__)


def load_sale_data(input_sale_file):
    with open(input_sale_file) as f:
        sale_data = csv.reader(f)
        sales = []
        for sale_row in sale_data:
            sales.append(Item(
                item_id=sale_row[0],
                country=sale_row[1],
                city=sale_row[2],
                sale_timestamp=sale_row[3],
                price=sale_row[4]
            ))

        return sales


if __name__ == "__main__":
    # TODO test Item

    i = Item(item_id='123',
             country='BG',
             city='Sofia',
             # sale_timestamp='2015-12-01T07:00:48+01:00',
             sale_timestamp=datetime.now(),
             price='987')
    print(i)
