library = {
    "book1": {
        "title": "Python Crash Course",
        "author": "Eric Matthes",
        "year": 2015,
        "rating": 4.7,
        "tags": ["Python", "Beginner", "Programming"]
    },
    "book2": {
        "title": "Machine Learning Basics",
        "author": "John Doe",
        "year": 2018,
        "rating": 4.5,
        "tags": ["AI", "ML", "Beginner"]
    },
    "book3": {
        "title": "Data Analytics Pro",
        "author": "Jane Smith",
        "year": 2020,
        "rating": 4.6,
        "tags": ["Data", "Python", "Analytics"]
    }
}

print(f"details of each book {library ['book1']}")
print(f"details of each book {library ['book2']}")
print(f"details of each book {library ['book3']}")

for key, value in library.items():
    if isinstance (value, dict):
        print(f"{key}")
    for sub_key, sub_value in value.items():
        print(f"title {value ['title']}")
        print(f"author {value ['author']}")
        print(f"year {value ['year']}")
        print(f"ratings {value ['rating']}")
        print(f"tags {value ['tags']}")