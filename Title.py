cities = ["new york", "london", "paris", "tokyo", "sydney"]
for city in cities:
    print("Cities in title case:", city.title())
    print("All cities in upper case:", city.upper())

for city in cities:
    if len(city) > 5:
        print(city)

print(len(cities))