with open("employees.txt", "r") as f:
    for line in f:
        print(line.strip()) #removes \n