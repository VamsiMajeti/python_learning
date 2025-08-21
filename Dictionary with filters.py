products = {
    "Laptop": 85000,
    "Phone": 55000,
    "Tablet": 30000,
    "Headphones": 5000,
    "Smartwatch": 12000
}
#Find and print the cheapest and most expensive product.
chepest_product = min(products, key = products.get)
print(chepest_product)
expensive_product = max(products, key = products.get)
print(expensive_product)
for i in products:
    products.items + int(1.5)
    print(products)