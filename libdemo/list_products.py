import json

with open("products.json", "rt") as f:
    products = json.load(f)   # Load JSON from file and return list[dict]

for product in products:
    print(f"{product['name']} - {product['price']}")
    for f in product['features']:
        print(f)

