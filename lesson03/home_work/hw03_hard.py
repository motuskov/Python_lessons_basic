import os


# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3


# Решение задания-1
def parse_fraction(fraction):
    space_index = fraction.find(" ")
    slash_index = fraction.find("/")
    if space_index != -1 and slash_index != -1:
        return [int(fraction[:space_index]),
                int(fraction[space_index + 1:slash_index]),
                int(fraction[slash_index + 1:])]
    elif slash_index != -1:
        return [0,
                int(fraction[:slash_index]),
                int(fraction[slash_index + 1:])]
    elif space_index == -1 and slash_index == -1:
        return [int(fraction),
                0,
                1]


def whole_to_numerator(fraction):
    fraction[1] += abs(fraction[0]) * fraction[2]
    if fraction[0] < 0:
        fraction[1] = -fraction[1]
    return fraction


def fraction_operation(fraction1, fraction2, operation):
    # Приводим дроби к одному знаменателю
    if fraction1[2] != fraction2[2]:
        fraction1[1] *= fraction2[2]
        fraction2[1] *= fraction1[2]
        fraction1[2] = fraction2[2] = fraction1[2] * fraction2[2]

    # Выполняем операцию
    result_fraction = [operation(fraction1[0], fraction2[0]),
                       operation(fraction1[1], fraction2[1]),
                       fraction1[2]]

    return result_fraction


def simplify_fraction(fraction):
    # Производим выделение целой части дроби
    fraction[0] = abs(fraction[1]) // fraction[2]
    if fraction[1] < 0:
        fraction[0] = -fraction[0]
    fraction[1] = abs(fraction[1]) % fraction[2]

    # Упрощаем дробь (алгоритм Евклида)
    a = fraction[1]
    b = fraction[2]
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    nod = a + b
    fraction[1] //= nod
    fraction[2] //= nod

    return fraction


def task_1(expr):
    # Выделяем операнды и операцию
    if expr.find(" + ") != -1:
        operands = expr.split(" + ")
        operation = True
    elif expr.find(" - ") != -1:
        operands = expr.split(" - ")
        operation = False

    # Производим разбор дробей
    fraction1 = parse_fraction(operands[0])
    fraction2 = parse_fraction(operands[1])

    # Приводим целую часть к числителю
    fraction1 = whole_to_numerator(fraction1)
    fraction2 = whole_to_numerator(fraction2)

    # Производим операцию над дробями
    result_fraction = fraction_operation(fraction1,
                                         fraction2,
                                         (lambda x, y: x + y) if operation else (lambda x, y: x - y))

    # Упрощаем дробь
    simplified_result_fraction = simplify_fraction(result_fraction)

    # Возвращаем значение
    if simplified_result_fraction[1] == 0:
        return simplified_result_fraction[0]
    elif simplified_result_fraction[0] == 0:
        return "{}/{}".format(simplified_result_fraction[1], simplified_result_fraction[2])
    else:
        return "{} {}/{}".format(simplified_result_fraction[0],
                                 simplified_result_fraction[1],
                                 simplified_result_fraction[2])


print(task_1("5/6 + 4/7"))
print(task_1("-2/3 - -2"))
print(task_1(input("Введите выражение с дробями: ")))


# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"


# Решение задания-2
def get_indexes(line, fields):
    indexes = []
    for field in fields:
        indexes.append(line.find(field))

    return indexes


def parse_line(line, indexes):
    # Разделяем строку на поля
    fields = []
    for i in range(0, len(indexes)):
        if i == len(indexes) - 1:
            fields.append(line[indexes[i]:].rstrip().lstrip())
        else:
            fields.append(line[indexes[i]:indexes[i+1]].rstrip().lstrip())

    return fields


def calc_salary(worker_info, hours):
    if worker_info[1] >= hours:
        return worker_info[0] / worker_info[1] * hours
    else:
        return worker_info[0] + worker_info[0] / worker_info[1] * (hours - worker_info[1]) * 2


def task_2(workers_file, hours_of_file):
    # Считываем информацию о работниках
    workers = {}
    with open(workers_file, 'r', encoding='UTF-8') as f:
        lines = f.readlines()
        workers_file_indexes = get_indexes(lines[0], ("Имя", "Фамилия", "Зарплата", "Должность", "Норма_часов"))
        for i in range(1, len(lines)):
            workers_file_fields = parse_line(lines[i], workers_file_indexes)
            workers["{} {}".format(workers_file_fields[0], workers_file_fields[1])] = \
                (int(workers_file_fields[2]), int(workers_file_fields[4]))

    # Считываем информацию об отработанных часах
    hours_of = {}
    with open(hours_of_file, 'r', encoding='UTF-8') as f:
        lines = f.readlines()
        hours_of_file_indexes = get_indexes(lines[0], ("Имя", "Фамилия", "Отработано часов"))
        for i in range(1, len(lines)):
            hours_of_file_fields = parse_line(lines[i], hours_of_file_indexes)
            hours_of["{} {}".format(hours_of_file_fields[0], hours_of_file_fields[1])] = int(hours_of_file_fields[2])

    # Рассчитываем зарплаты
    salary = {}
    for worker in workers:
        salary[worker] = round(calc_salary(workers[worker], hours_of[worker]), 2)

    return salary


print(task_2("data/workers", "data/hours_of"))


# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# # Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))


# Решение задания-3
def task_3(fruits_file, chars):
    with open(fruits_file, 'r', encoding='UTF-8') as f:
        for line in f:
            if line[0] in chars:
                with open("data/fruits_{}".format(line[0]), 'a', encoding='UTF-8') as fruits_file:
                    fruits_file.write(line)


task_3("data/fruits.txt", list(map(chr, range(ord('А'), ord('Я')+1))))
