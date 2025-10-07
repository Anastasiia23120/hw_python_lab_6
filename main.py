# Автор: Медведь А.Б. (перший студент)
# Програма для роботи зі словником студентів

# Створюємо словник з інформацією про студентів
students = {
    1: {
        "group": "КН-44/1",
        "name": "Ющенко Альона Володимирівна",
        "course": 2,
        "subjects": {
            "Математика": 85,
            "Програмування": 92,
            "Фізика": 99
        }
    },
    2: {
        "group": "КН-44/1",
        "name": "Могильний Дмитро Валерійович",
        "course": 2,
        "subjects": {
            "Математика": 74,
            "Програмування": 88,
            "Фізика": 81
        }
    },
    3: {
        "group": "КН-44/1",
        "name": "Мигаль Яна Іванівна",
        "course": 2,
        "subjects": {
            "Математика": 85,
            "Програмування": 91,
            "Фізика": 88
        }
    },
    4: {
        "group": "КН-44/1",
        "name": "Пікульов Іван Юрійович",
        "course": 4,
        "subjects": {
            "Математика": 81,
            "Програмування": 93,
            "Фізика": 98
        }
    },
    5: {
        "group": "КН-44/2",
        "name": "Свистюр Дмитро Сергійович",
        "course": 1,
        "subjects": {
            "Математика": 82,
            "Програмування": 99,
            "Фізика": 78
        }
    },
}

# Функція для додавання нового студента
def add_student(students, student_id, group, name, course, subjects):
    """
    Додає нового студента до словника.
    :param students: основний словник
    :param student_id: унікальний ID студента
    :param group: номер групи
    :param name: ПІБ студента
    :param course: курс навчання
    :param subjects: словник з предметами та оцінками
    """
    students[student_id] = {
        "group": group,
        "name": name,
        "course": course,
        "subjects": subjects
    }

# Приклад використання функції
add_student(
    students,
    3,
    "КН-44/1",
    "Сидоренко Олег Олексійович",
    3,
    {"Математика": 90, "Програмування": 95, "Фізика": 89}
)

# Вивід результатів
for sid, info in students.items():
    print(f"ID: {sid}")
    print(f"Група: {info['group']}")
    print(f"ПІБ: {info['name']}")
    print(f"Курс: {info['course']}")
    print("Оцінки:")
    for subject, grade in info['subjects'].items():
        print(f"  {subject}: {grade}")
    print("-" * 30)

# Автор: Пікульов Іван Юрійович (другий студент)
# Додано функцію для сортування студентів за прізвищем

def sort_students_by_lastname(students):
    """
    Повертає словник студентів, відсортований за прізвищем.
    :param students: словник студентів
    :return: новий словник у відсортованому порядку
    """
    sorted_items = sorted(students.items(), key=lambda item: item[1]["name"].split()[0])
    return dict(sorted_items)

# Виклик функції сортування та повний вивід результатів
print("\nСортування студентів за прізвищем:\n")
sorted_students = sort_students_by_lastname(students)

for sid, info in sorted_students.items():
    print(f"ID: {sid}")
    print(f"ПІБ: {info['name']}")
    print(f"Група: {info['group']}")
    print(f"Курс: {info['course']}")
    print("Оцінки:")
    for subject, grade in info['subjects'].items():
        print(f"  {subject}: {grade}")
    print("-" * 30)