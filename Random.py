import random
cities = ["Hyderabad", "Amaravathi", "Chennai", "Panjim", "Mumbai"]
city = random.choice(cities)
temperature = random.randint(20,40)
print(f"Today's temperature in {city} is {temperature}C")