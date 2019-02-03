# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


# Решение задания-1
class School:
    def __init__(self, name):
        self.name = name


class SchoolClass:
    def __init__(self, name, school, teachers=[]):
        self.name = name
        self.school = school
        self.teachers = teachers

    def get_teachers(self):
        return list(map(lambda x: x.name, self.teachers))


class Person:
    def __init__(self, name, mother=None, father=None):
        self.name = name
        self.mother = mother
        self.father = father

    def get_parents(self):
        return self.mother.name, self.father.name


class Pupil(Person):
    def __init__(self, name, mother, father, school_class):
        Person.__init__(self, name, mother, father)
        self.school_class = school_class


class Teacher(Person):
    def __init__(self, name, subject):
        Person.__init__(self, name)
        self.subject = subject


class Subject:
    def __init__(self, name):
        self.name = name


def find_school_classes(school_classes, school_name):
    return list(map(lambda x: x.name, list(filter(lambda x: x.school.name == school_name, school_classes))))


def find_class_pupils(school_classes, pupils, school_name, class_name):
    for school_class in school_classes:
        if school_class.name == class_name and school_class.school.name == school_name:
            return list(map(lambda x: x.name, list(filter(lambda x: x.school_class == school_class, pupils))))


def find_pupil_subjects(pupils, pupil_name):
    for pupil in pupils:
        if pupil.name == pupil_name:
            return list(map(lambda x: x.subject.name, pupil.school_class.teachers))


def find_pupil_parents(pupils, pupil_name):
    for pupil in pupils:
        if pupil.name == pupil_name:
            return pupil.get_parents()


def find_class_teachers(school_classes, school_name, class_name):
    for school_class in school_classes:
        if school_class.name == class_name and school_class.school.name == school_name:
            return school_class.get_teachers()


schools = [School("Школа №1"),
           School("Школа №2")]

subjects = [Subject("Математика"),
            Subject("Русский язык"),
            Subject("История")]

teachers = [Teacher("Белоусов А.А.", subjects[0]),
            Teacher("Сафронова Г.В.", subjects[1]),
            Teacher("Белова В.В.", subjects[2])]

schoolClasses = [SchoolClass("5Б", schools[0], [teachers[0], teachers[1]]),
                 SchoolClass("4А", schools[0], [teachers[1], teachers[2]]),
                 SchoolClass("2А", schools[1], [teachers[0], teachers[2]]),
                 SchoolClass("8В", schools[1], [teachers[0], teachers[1], teachers[2]])]

pupils = [Pupil("Иванов К.В.", Person("Иванова И.С."), Person("Иванов А.К."), schoolClasses[0]),
          Pupil("Федотов К.В.", Person("Федотова И.С."), Person("Федотов А.К."), schoolClasses[0]),
          Pupil("Константинова К.В.", Person("Константинова И.С."), Person("Константинов А.К."), schoolClasses[0]),
          Pupil("Бондарчук К.В.", Person("Бондарчук И.С."), Person("Бондарчук А.К."), schoolClasses[1]),
          Pupil("Луговой К.В.", Person("Луговая И.С."), Person("Луговой А.К."), schoolClasses[1]),
          Pupil("Патрушев К.В.", Person("Патрушева И.С."), Person("Патрушев А.К."), schoolClasses[1]),
          Pupil("Сидорова К.В.", Person("Сидорова И.С."), Person("Сидоров А.К."), schoolClasses[2]),
          Pupil("Ромашов К.В.", Person("Ромашова И.С."), Person("Ромашов А.К."), schoolClasses[2]),
          Pupil("Степанов К.В.", Person("Степанова И.С."), Person("Степанов А.К."), schoolClasses[2]),
          Pupil("Хац К.В.", Person("Хац И.С."), Person("Хац А.К."), schoolClasses[3]),
          Pupil("Матвеенко К.В.", Person("Матвеенко И.С."), Person("Матвеенко А.К."), schoolClasses[3]),
          Pupil("Крюкова К.В.", Person("Крюкова И.С."), Person("Крюков А.К."), schoolClasses[3])]

# Выводим список всех классов школы
print(f"Список всех классов школы №2: {find_school_classes(schoolClasses, 'Школа №2')}")

# Выводим список всех учеников класса
print(f"Список всех учеников класса 2А школы №2: {find_class_pupils(schoolClasses, pupils, 'Школа №2', '2А')}")

# Выводим список всех предметов ученика
print(f"Список всех предметов ученика Луговой К.В.: {find_pupil_subjects(pupils, 'Луговой К.В.')}")

# Выводим ФИО родителей ученика
print(f"ФИО родителей ученика Матвеенко К.В.: {find_pupil_parents(pupils, 'Матвеенко К.В.')}")

# Выводим список учителей, преподающих в классе
print(f"Список учителей, преподающих в классе: {find_class_teachers(schoolClasses, 'Школа №2', '2А')}")
