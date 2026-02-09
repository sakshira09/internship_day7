import csv

with open("C:\\Users\\saksh\\DS_AI_Internship\\day3\\day5\\day6\\students.csv", "r") as file:
    reader = csv.DictReader(file) 

    print("Students who Passed:\n")

    for row in reader:
        if row["Status"] == "Pass":
            print(row["Name"])