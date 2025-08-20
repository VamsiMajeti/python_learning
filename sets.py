developers = {"Alice", "Bob", "Charlie", "David", "Eve"}
designers = {"Charlie", "Eve", "Frank", "Grace"}
developers.add("Helen")
designers.add("Ivy")
designers.add("Jack")
designers.remove("Grace")
print(developers|designers)
print(developers & designers)
print(developers - designers)
print(developers ^ designers)
print("\n--- Checking membership ---")
for person in developers | designers:  # loop over the union
    if person in developers and person in designers:
        print(person, "is in both")
    else:
        print(person, "is only in one")