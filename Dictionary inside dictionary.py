books = {
    "book1": {
        "title": "Python 101",
        "author": "John Doe",
        "year": 2019
    },
    "book2": {
        "title": "AI for Beginners",
        "author": "Jane Smith",
        "year": 2020
    },
    "book3": {
        "title": "Data Analytics",
        "author": "Alice Brown",
        "year": 2021
    }
}

print(f"Author of book 2 is {books ['book2'] ['author']}")
books ["book3"] ["year"] = 2025
books ["book1"] ["rating"] = 4.5
books ["book2"] ["rating"] = 4.3
books ["book3"] ["rating"] = 4.1
for key, value in books.items():
    if isinstance(value, dict):
        print(f"{key}:")
        print(f"Title {value['title']}")
        print(f"author {value['author']}")
        print(f"year {value['year']}")
        print(f"rating {value['rating']}")