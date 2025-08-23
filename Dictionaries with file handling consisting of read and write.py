import csv

with open("books_dict.csv", "w", newline="") as f:
    field_names = ["title", "author", "year"]
    writer= csv.DictWriter(f, fieldnames=field_names)
    writer.writeheader()
    writer.writerow({"title":"Python 101", "author":"John Doe", "year":2019})
    writer.writerow({"title":"AI for beginners", "author": "Jane Smith", "year": 2021})
    writer.writerow({"title":"data analytics pro", "author":"Alice Brown", "year":2020})

with open("books_dict.csv", "r") as f:
    reader = csv.Dictreader(f)
    for row in reader:
        print(row)
        print()