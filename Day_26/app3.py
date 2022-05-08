import random
students = ["Marie", "Ibrahima", "Sofia", "Babacar", "Coumba"]

new_students = {student: random.randint(1, 100) for student in students}
print(new_students)

pass_students = {student: score for (student, score) in new_students.items() if score >= 10}
print(pass_students)