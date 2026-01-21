groupmates = [
    {
        "name": "Александр",
        "surname": "Иванов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Иван",
        "surname": "Петров",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 5]
    }
]


def print_students(students):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20))
    for student in students:
        print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30),
              str(student["marks"]).ljust(20))


def filter_students_by_average(students, min_average):
    filtered = []
    for student in students:
        average = sum(student["marks"]) / len(student["marks"])
        if average > min_average:
            filtered.append(student)
    return filtered

print("Все студенты:")
print_students(groupmates)

print("\n" + "=" * 80 + "\n")
min_avg = float(input("Введите минимальный средний балл: "))
filtered_students = filter_students_by_average(groupmates, min_avg)

if filtered_students:
    print(f"\nСтуденты со средним баллом выше {min_avg}:")
    print_students(filtered_students)
else:
    print(f"\nНет студентов со средним баллом выше {min_avg}")