# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()


# Решение задачи-1
fruits = ["яблоко", "банан", "киви", "арбуз"]

# Определяем максимальную длину слова в списке
maxFruitLen = 0
for fruit in fruits:
    if len(fruit) > maxFruitLen:
        maxFruitLen = len(fruit)

# Выводим нумерованный список фруктов с выравниванием по правой стороне
i = 1
for fruit in fruits:
    spacesNeeded = " " * (maxFruitLen - len(fruit))
    print("{}. {}{}".format(i, spacesNeeded, fruit))
    i += 1


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.


# Решение задачи-2
list1 = ["яблоко", "банан", "киви", "арбуз"]
list2 = ["банан", "киви"]

for list2Elem in list2:
    list1.remove(list2Elem)

print(list1)


# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.


# Решение задачи-3 (вариант-1)
numbers = [51, 69, 12, 78, 65, 2, 999]

newNumbers = []
for number in numbers:
    if number % 2 == 0:
        newNumbers.append(number / 4)
    else:
        newNumbers.append(number * 2)

print(newNumbers)


# Решение задачи-3 (вариант-2)
numbers = [51, 69, 12, 78, 65, 2, 999]

newNumbers = []
for number in numbers:
    newNumbers.append(number / 4 if number % 2 == 0 else number * 2)

print(newNumbers)
