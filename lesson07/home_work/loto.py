import random


#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""


# Решение
class Card:
    def __init__(self, card_holder):
        self.card_holder = card_holder
        rand_numbers = random.sample(range(1, 91), k=15)
        self.numbers = [rand_numbers[:5], rand_numbers[5:10], rand_numbers[10:]]
        for line in self.numbers:
            line.sort()
            for i in range(4):
                line.insert(random.randint(0, len(line)), None)

    def __str__(self):
        card_str = f"{self.card_holder:^36}\n"
        for line in self.numbers:
            for cell in line:
                card_str += f"{str(cell if cell else ''):^4}"
            card_str += f"\n"
        card_str += f"-" * 36
        return card_str

    def cross_out(self, number):
        for line in self.numbers:
            try:
                line[line.index(number)] = "-"
                return True
            except ValueError:
                continue
        return False

    def go_on(self, number):
        return number not in self.numbers[0] and number not in self.numbers[1] and number not in self.numbers[2]

    def have_numbers(self):
        for line in self.numbers:
            for cell in line:
                if isinstance(cell, int):
                    return True
        return False


class KegsBag:
    def __init__(self):
        self.kegs = list(range(1, 91))
        random.shuffle(self.kegs)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return self.kegs.pop()
        except IndexError:
            raise StopIteration

    def __len__(self):
        return len(self.kegs)


# Создаем карточки игроков
userCard = Card("Ваша карточка")
computerCard = Card("Карточка компьютера")

# Создаем мешок с бочонками
kegsBag = KegsBag()

# Играем
for keg in kegsBag:
    # Выводим информацию текущего хода
    print(f"\nНовый бочонок: {keg} (осталось {len(kegsBag)})\n\n{userCard}\n\n{computerCard}")

    # Принимаем ответ пользователя
    userAnswer = ""
    while userAnswer not in ["y", "n"]:
        userAnswer = input("Зачеркнуть число? (y/n) ")

    # Анализируем ответ пользователя
    if userAnswer == "y":
        if not userCard.cross_out(keg):
            print(f"В вашей карточке нет числа {keg}. Вы проиграли.")
            break
    else:
        if not userCard.go_on(keg):
            print(f"В вашей карточке есть число {keg}. Вы проиграли.")
    if not userCard.have_numbers():
        print(f"Поздравляем! Вы выиграли.")
        break

    # Анализируем карточку компьютера
    computerCard.cross_out(keg)
    if not computerCard.have_numbers():
        print(f"Компьютер вычеркнул все числа. Вы проиграли.")
        break

print("Игра окончена.")
