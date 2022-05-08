my_list = [1, 2, 3, 4, 5, 6]
new_list = [n * 2 for n in my_list]
print(new_list)

names = ["Alex", "Caroline", "Alexandra", "Abou", "Moussa", "Marie", "Ibrahima", "Sofia", "Babacar", "Coumba"]
short_names = [name for name in names if len(name) <= 5]
print(short_names)

long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)