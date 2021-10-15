import csv


with open("departement.csv", "r") as dept:
    read = csv.reader(dept, delimiter=",")
    for row in read:
        print(row)

