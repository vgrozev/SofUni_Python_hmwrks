
import csv

COLUMN_ITEM_ID = 0
COLUMN_CATEGORY = 5


def load_catalog(filename: str) -> dict:
    """
        Expected columns in catalog file:

            1. Идентификационен номер на артикула;
            2. Наименование на артикула;
            3. Цветове, в които артикулът е наличен;
            4. Група на артикула;
            5. Спорт, за който е предназначен артикулът;
            6. Категория
            7. Подкатегория
            8. Пол, за който е предназначен артикула - мъже, жени, unisex, деца, бебета


        Result:
            {
                item_id : category name
                "J11328": "SHOES"
            }

    """

    result = {}
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            item_id = row[COLUMN_ITEM_ID]
            category = row[COLUMN_CATEGORY]
            result[item_id] = category
    return result
