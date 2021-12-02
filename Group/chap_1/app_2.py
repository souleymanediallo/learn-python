import csv

with open("departement.csv", "r") as dept:
    read = csv.reader(dept, delimiter=",")
    departments = set(d[2] for d in read)

if "Côtes-d'armor" in departments:
    departments.remove("Côtes-d'armor")

print(departments)


