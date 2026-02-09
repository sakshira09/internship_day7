file = open("day3/day5/day6/example.txt", "r+")
print(file.read())
print(file.readline())
print(file.readline())
file.write("\n This is a new line.")
file.close()
with open("day3/day5/day6/image.png", "rb") as f:
    image = f.read()
    print(type(image))
    print(len(image))
try:
    file = open("day3/day5/day6/ex.txt", "r")
    print(file.read())
# except FileNotFoundError:
#     print("File not found, plz open the existing file .")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    file.close()
