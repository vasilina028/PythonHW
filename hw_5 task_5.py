# 1) Создание словаря data
data = {
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "Age": [20, 21, 22, 20, 23],
    "Department": ["Math", "Physics", "CS", "Math", "CS"],
    "GPA": [3.9, 3.5, 3.8, 3.7, 3.6],
    "Credits": [30, 28, 32, 30, 26]
}

# 2) Фильтрация данных
print("Студенты с GPA выше 3.7:")
high_gpa_students = [student for student in data["Name"] if data["GPA"][data["Name"].index(student)] > 3.7]
print(high_gpa_students)

print("\nСтуденты с кафедры 'Math':")
math_students = [student for student in data["Name"] if data["Department"][data["Name"].index(student)] == "Math"]
print(math_students)

# 3) Сортировка
print("\nСтуденты, отсортированные по возрасту:")
sorted_by_age = sorted(data["Name"], key=lambda x: data["Age"][data["Name"].index(x)])
print(sorted_by_age)

print("\nСтуденты, отсортированные по GPA в порядке убывания:")
sorted_by_gpa = sorted(data["Name"], key=lambda x: data["GPA"][data["Name"].index(x)], reverse=True)
print(sorted_by_gpa)

# 4) Группировка данных
print("\nСредний GPA студентов по кафедрам:")
avg_gpa_by_dept = {dept: sum(gpa for i, gpa in enumerate(data["GPA"]) if data["Department"][i] == dept) / sum(1 for i, d in enumerate(data["Department"]) if d == dept) for dept in set(data["Department"])}
print(avg_gpa_by_dept)

print("\nКоличество студентов в каждой кафедре:")
student_count_by_dept = {dept: sum(1 for d in data["Department"] if d == dept) for dept in set(data["Department"])}
print(student_count_by_dept)

# 5) Добавление столбца Internship
data["Internship"] = [True, False, None, True, None]
print("\nСтроки с пропущенными значениями в столбце Internship:")
print([student for student, internship in zip(data["Name"], data["Internship"]) if internship is None])
data["Internship"] = [False if internship is None else internship for internship in data["Internship"]]

# 6) Добавление столбца Final Credits
data["Final Credits"] = [credits * gpa for credits, gpa in zip(data["Credits"], data["GPA"])]
print("\nОбновленная таблица:")
print(data)

# 7) Использование индексации
print("\nДанные о втором студенте:")
print({k: v[1] for k, v in data.items()})

print("\nИмена и GPA первых трех студентов:")
print({
    "Name": [data["Name"][i] for i in range(3)],
    "GPA": [data["GPA"][i] for i in range(3)]
})

print("\nИзменение GPA у четвертого студента:")
data["GPA"][3] = 3.95
print(data)

print("\nПоследние два столбца для всех студентов:")
print({
    "Final Credits": data["Final Credits"],
    "Internship": data["Internship"]
})