products = {
    "Laptop": 85000,
    "Phone": 55000,
    "Tablet": 30000,
    "Headphones": 5000,
    "Smartwatch": 12000
}
for key in products:
    print("Keys:", key)
for value in products.values():
    print("Values:", value)
for key, value in products.items():
    print("Key:", key, "costs", "value", value)
print("Total value of all the products is", sum(products.values()))
print("Most expensive product is", max(products.values()))