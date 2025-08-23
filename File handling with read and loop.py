with open ("employees.txt", "r") as f:
    for line in f:
        name, department, salary = line.strip().split(",")
        print(f"Name: {name} | Department: {department} | salary: {salary}")