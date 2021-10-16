import csv


with open("departement.csv", "r") as dept:
    read = csv.reader(dept, delimiter=",")
    departments = []
    for row in read:
        departments.append(row[2])

l1 = [i.title() for i in departments]
print(l1)

# join transforme une liste en chaine de caractère
print(len((','.join(l1))))

# l1 = []
# for i in departments:
#     l1.append(i.upper())
#
# print(l1)

# l1 = list(map(lambda d: d.upper(), departments))
# l2 = list(filter(lambda d: d[0] in ["A", "H", "J"], departments))

#print(l1)
#print(l2)

# print(departments)
# departments[2:2] = ["Neuchatel", "Jura"]
# del departments[2]
# del departments[2]
# departments.remove("Jura")
# departments.sort(key=lambda l: l[-1])
# departments.sort(key=lambda l: l[::-1])
# departments += "Neuchatel"
# l1, *l2 = departments
# l1 = departments[-len("Neuchatel"):]
# print(''.join(l1))
