# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

equation = 'y = -12x + 11111140.2121'
x = 2.5
# вычислите и выведите y


# Решение задания-1
xIndex = equation.find("x")
k = float(equation[4:xIndex])
b = float(equation[xIndex + 4:])
y = k * x + b

print("y =", y)


# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом 
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
date = '01.11.1985'

# Примеры некорректных дат
date = '01.22.1001'
date = '1.12.1001'
date = '-2.10.3001'


# Решение задания-2
date = input("Введите дату: ")
monthsDur = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if len(date) != 10:
    print("Длина строки не соответствует формату")
elif not date[-4:].isdigit() or int(date[-4:]) not in range(1, 9999):
    print("Год не соответствует заданному формату")
elif not date[3:5].isdigit() or int(date[3:5]) not in range(1, 12):
    print("Месяц не соответствует заданному формату")
elif not date[:2].isdigit() or int(date[:2]) not in range(1, monthsDur[int(date[3:5])]):
    print("День не соответствует заданному формату")
else:
    print("Дата введена корректно")


# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты, 
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3


# Решение задания-3
room = int(input("Введите номер комнаты: "))

# Находим номер блока, номер первого этажа блока и номер первой комнаты блока
# Блок - множество этажей с одинаковым количеством комнат
block = 1
blockMaxFloor = 1
blockMaxRoom = 1
while blockMaxRoom < room:
    block += 1
    blockMaxFloor += block
    blockMaxRoom += block ** 2
blockFirstFloor = blockMaxFloor - block + 1
blockFirstRoom = blockMaxRoom - block ** 2 + 1

# Находим количество комнат на этаже блока
blockFloorRoomCount = block ** 2 / block

# Находим номер этажа в блоке
blockFloor = (room - blockFirstRoom) // blockFloorRoomCount

# Находим номер этажа и номер комнаты на этаже
roomFloor = int(blockFirstFloor + blockFloor)
roomFloorNumb = int(room - blockFirstRoom - blockFloor * blockFloorRoomCount + 1)

print(roomFloor, roomFloorNumb)
