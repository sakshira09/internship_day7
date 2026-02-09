name = input("Enter your name: ")
goal = input("Enter your Daily Goal: ")

with open("C:\\Users\\saksh\\DS_AI_Internship\\day3\\day5\\day6\\journal.txt", "a") as file:
    file.write(name + " - " + goal + "\n")
print("Your goal has been saved to the journal.")
# import os

# name = input("Enter your name: ")
# goal = input("Enter your Daily Goal: ")

# print("Python is running from:")
# print(os.getcwd())

# with open("ex.txt", "a") as file:
#     file.write(name + " - " + goal + "\n")

# print("Data written successfully")

