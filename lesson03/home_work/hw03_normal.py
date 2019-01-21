import math


PHI = (1 + math.sqrt(5)) / 2    # Золотое сечение ряда Фибоначчи


# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1


# Решение задания-1, вариант-1 (вычисление элементов по формуле Бине)
def fibonacci_1(n, m):
    fibonacci_row = []
    for i in range(n, m + 1):
        fibonacci_row.append(round(PHI**i / math.sqrt(5)))
    return fibonacci_row


# Решение задания-1, вариант-2 (вычисление элементов по определению ряда Фибоначчи)
def fibonacci_2(n, m):
    fibonacci_row = [0, 1]
    for i in range(2, m + 1):
        fibonacci_row.append(fibonacci_row[i-1] + fibonacci_row[i-2])
    return fibonacci_row[n:]


print(fibonacci_1(5, 9))
print(fibonacci_2(5, 9))


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


# Решение задачи-2
def sort_to_max(origin_list):
    exchange = True
    while exchange:
        exchange = False
        for i in range(0, len(origin_list) - 1):
            if origin_list[i] > origin_list[i + 1]:
                origin_list[i], origin_list[i + 1] = origin_list[i + 1], origin_list[i]
                exchange = True
    return origin_list


print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


# Решение задачи-3
def my_filter(func, iterable):
    output_list = []
    for i in iterable:
        if func(i):
            output_list.append(i)
    return output_list


print(my_filter(lambda x: x > 0, [-5, 2, 9, -62, 0, 12]))


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.


# Решение задачи-4 (введено упрощение: A1A2 и A1A3 - смежные стороны параллелограмма)
def segment_len(a1, a2):
    return math.sqrt((a1[0]-a2[0])**2 + (a1[1]-a2[1])**2)


def is_parallelogram(a1, a2, a3, a4):
    return segment_len(a1, a2) == segment_len(a3, a4) and segment_len(a2, a3) == segment_len(a1, a4)


print(is_parallelogram((1, 1), (2, 3), (7, 3), (6, 1)))
