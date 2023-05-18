with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

a = 0

with open("new_file.txt", "w") as file:
    file.write(f"\n{a}")
