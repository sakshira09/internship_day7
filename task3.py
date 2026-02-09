filename = input("Enter the filename: ")

try:
    with open(filename, "r") as file:
        print(file.read())
except FileNotFoundError:
    print("Oops! That file doesn't exist yet")
