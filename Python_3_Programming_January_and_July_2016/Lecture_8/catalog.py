import csv


class CatalogItem(object):

    def __init__(self, item_id, name, colors, group, sport_type, category, subcategory, age_type):
        self.item_id = str(item_id)
        self.name = str(name)
        self.colors = str(colors)
        self.group = str(group)
        self.sport_type = str(sport_type)
        self.category = str(category)
        self.subcategory = str(subcategory)
        self.age_type = str(age_type)

    def __repr__(self):
        return "{} : {}".format(self.__class__.__name__, str(self.__dict__))


def load_catalog_by_item_id(input_file_catalog):
    with open(input_file_catalog) as f:
        catalog_data = csv.reader(f)

        catalog = {}  # item_id: CategoryItem
        for catalog_row in catalog_data:
            # print(catalog_row)
            catalog[catalog_row[0]] = CatalogItem(
                item_id=catalog_row[0],
                name=catalog_row[1],
                colors=catalog_row[2],
                group=catalog_row[3],
                sport_type=catalog_row[4],
                category=catalog_row[5],
                subcategory=catalog_row[6],
                age_type=catalog_row[7]
            )

        return catalog


# if __name__ == "__main__":
#