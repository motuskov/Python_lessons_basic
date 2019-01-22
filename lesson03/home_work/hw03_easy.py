# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.


# Решение задания-1, вариант-1 (с использованием строк)
def my_round_1(number, ndigits):
    # Отбрасываем ту часть знаков после запятой, которую необходимо округлить.
    number_str = str(number)
    ndigit_index = number_str.find(".") + ndigits + 1
    rounded_number = float(number_str[:ndigit_index])

    # Учитываем первый знак отброшенной части.
    next_digit = number_str[ndigit_index:ndigit_index + 1]
    if next_digit.isdigit() and int(next_digit) >= 5:
        if ndigits == 0:
            rounded_number += 1
        else:
            rounded_number += float("0.{}1".format("0" * (ndigits - 1)))

    return rounded_number


# Решение задания-1, вариант-2 (с использованием математических операций)
def my_round_2(number, ndigits):
    # Отбрасываем ту часть знаков после запятой, которую необходимо округлить.
    rounded_number = number * 10**ndigits // 1 / 10**ndigits

    # Учитываем первый знак отброшенной части.
    next_digit = number * 10**(ndigits+1) // 1 % 10
    rounded_number += int(next_digit >= 5) / 10**ndigits

    return rounded_number


print(my_round_1(2.1234567, 5))
print(my_round_1(2.1999967, 5))
print(my_round_1(2.9999967, 5))
print(my_round_2(2.1234567, 5))
print(my_round_2(2.1999967, 5))
print(my_round_2(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить


# Решение задания-2, вариант-1
def lucky_ticket_1(ticket_number):
    return sum(list(map(int, list(str(ticket_number % 1000))))) == sum(list(map(int, list(str(ticket_number // 1000)))))


# Решение задания-2, вариант-2
def lucky_ticket_2(ticket_number):
    digits = []
    while len(digits) < 6:
        digits.append(ticket_number % 10)
        ticket_number //= 10
    return sum(digits[:3]) == sum(digits[3:])


print(lucky_ticket_1(123006))
print(lucky_ticket_1(12321))
print(lucky_ticket_1(436751))
print(lucky_ticket_2(123006))
print(lucky_ticket_2(12321))
print(lucky_ticket_2(436751))
