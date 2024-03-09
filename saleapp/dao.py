import json


def get_categories():
    with open('data/categories.json', encoding='utf-8') as file:
        return json.load(file)


def get_products(q=None, category=None):
    with open('data/product.json', encoding='utf-8') as file:
        product = json.load(file)
        if category:
            product = [p for p in product if p['category_id'] == int(category)]
        if q:
            product = [p for p in product if p['name'].find(q) > 0]
        return product


def get_product_by_id(id):
    with open('data/product.json', encoding='utf-8') as file:
        product = json.load(file)
        for p in product:
            if p["id"] == int(id):
                return p
