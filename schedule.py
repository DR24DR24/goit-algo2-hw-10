# -*- coding: utf-8 -*-
"""
Created on Sun Feb  1 12:24:51 2026

@author: i5
"""

# Визначення класу Teacher
class Teacher:
    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = set(can_teach_subjects)
        self.assigned_subjects = set()

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"


def create_schedule(subjects, teachers):
    # Копія множини предметів, які ще треба покрити
    uncovered = set(subjects)

    # Список вибраних викладачів
    selected_teachers = []

    while uncovered:
        best_teacher = None
        best_cover = set()

        for teacher in teachers:
            # Які з непокритих предметів може викладати цей викладач
            can_cover = uncovered.intersection(teacher.can_teach_subjects)

            # Якщо цей викладач покриває більше предметів — беремо його
            if best_teacher is None or len(can_cover) > len(best_cover):
                best_teacher = teacher
                best_cover = can_cover

            # Якщо кількість однакова — обираємо молодшого
            elif len(can_cover) == len(best_cover) and best_teacher is not None:
                if can_cover and teacher.age < best_teacher.age:
                    best_teacher = teacher
                    best_cover = can_cover

        # Якщо жоден викладач не може покрити хоча б один новий предмет — вихід
        if best_teacher is None or not best_cover:
            return None  # неможливо покрити всі предмети

        # Призначаємо предмети цьому викладачу
        best_teacher.assigned_subjects = best_teacher.assigned_subjects.union(best_cover)

        # Прибираємо покриті предмети зі списку непокритих
        uncovered -= best_cover

        # Додаємо викладача в розклад (якщо ще не додали)
        if best_teacher not in selected_teachers:
            selected_teachers.append(best_teacher)

        # Щоб викладача не вибирали знову для тих самих предметів,
        # можна (опційно) прибрати вже призначені предмети з його можливостей:
        best_teacher.can_teach_subjects -= best_cover

    return selected_teachers


if __name__ == '__main__':
    # Множина предметів
    subjects = {'Математика', 'Фізика', 'Хімія', 'Інформатика', 'Біологія'}

    # Створення списку викладачів
    teachers = [
        Teacher("Олександр", "Іваненко", 45, "o.ivanenko@example.com",
                {'Математика', 'Фізика'}),

        Teacher("Марія", "Петренко", 38, "m.petrenko@example.com",
                {'Хімія'}),

        Teacher("Сергій", "Коваленко", 50, "s.kovalenko@example.com",
                {'Інформатика', 'Математика'}),

        Teacher("Наталія", "Шевченко", 29, "n.shevchenko@example.com",
                {'Біологія', 'Хімія'}),

        Teacher("Дмитро", "Бондаренко", 35, "d.bondarenko@example.com",
                {'Фізика', 'Інформатика'}),

        Teacher("Олена", "Гриценко", 42, "o.grytsenko@example.com",
                {'Біологія'}),
    ]

    # Виклик функції створення розкладу
    schedule = create_schedule(subjects, teachers)

    # Виведення розкладу
    if schedule:
        print("Розклад занять:\n")
        for teacher in schedule:
            print(f"{teacher.first_name} {teacher.last_name}, "
                  f"{teacher.age} років, email: {teacher.email}")
            print(f"   Викладає предмети: {', '.join(sorted(teacher.assigned_subjects))}\n")
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")