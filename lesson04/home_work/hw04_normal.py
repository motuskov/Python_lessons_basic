import re
import random


# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.

line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNO'\
       'GIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzK'\
       'TUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqn'\
       'LxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXa'\
       'pzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWete'\
       'kUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQ'\
       'WrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXb'\
       'JrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCC'\
       'EUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfB'\
       'tQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuT'\
       'SkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCu'\
       'UJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXB'\
       'qHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFa'\
       'XiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQ'\
       'zTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'


# Решение задания-1, вариант-1 (с помощью re)
def task_1_re(text):
    # Находим символы, которые лежат внутри символов в верхнем регистре
    between_capital = re.split(r"[A-Z]+", text)

    # Отфильтровываем символы, которые не являются символами в нижнем регистре
    result = list(filter(lambda x: re.match(r"[a-z]+", x), between_capital))

    return result


print(task_1_re(line))


# Решение задания-1, вариант-2 (без использования re)
def task_1_wo_re(text):
    lowercase_letters = list(map(chr, range(ord('a'), ord('z') + 1)))
    capital_letters = list(map(chr, range(ord('A'), ord('Z') + 1)))
    result = []
    prev_ch = ""
    word = ""
    for ch in text:
        if ch in lowercase_letters and (prev_ch in capital_letters or prev_ch == "" or len(word) > 0):
            word += ch
        elif ch in capital_letters and len(word) > 0:
            result.append(word)
            word = ""
        prev_ch = ch
    if len(word) > 0:
        result.append(word)
    return result


print(task_1_wo_re(line))


# Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа - два символа в верхнем регистре.
# Т.е. из строки 
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.

line_2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysm'\
       'NOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewV'\
       'fzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSA'\
       'HqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIV'\
       'jXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnW'\
       'etekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfC'\
       'vzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbR'\
       'uXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkm'\
       'jCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOn'\
       'LfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGS'\
       'euTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCf'\
       'KCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWH'\
       'uXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQN'\
       'JFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQ'\
       'oiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'


# Решение задания-2, вариант-1 (с помощью re)
def task_2_re(text):
    return re.findall(r"[a-z]{2}([A-Z]+)[A-Z]{2}", text)


print(task_2_re(line_2))


# Решение задания-2, вариант-2 (без использования re)
def task_2_wo_re(text):
    lowercase_letters = list(map(chr, range(ord('a'), ord('z') + 1)))
    capital_letters = list(map(chr, range(ord('A'), ord('Z') + 1)))
    result = []
    prev_ch = ""
    prev_prev_ch = ""
    word = ""
    for ch in text:
        if ch in lowercase_letters:
            if len(word) > 2:
                result.append(word[:-2])
            word = ""
        elif ch in capital_letters and \
                ((prev_ch in lowercase_letters and prev_prev_ch in lowercase_letters) or len(word) > 0):
            word += ch
        prev_prev_ch = prev_ch
        prev_ch = ch
    if len(word) > 2:
        result.append(word[:-2])
    return result


print(task_2_wo_re(line_2))


# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.


# Решение задания-3 (В числе может присутствовать не сколько последовательностей с одинаковой, максимальной длиной.
# Выводится только одна из них)
# В формулировке задачи есть неточность: "целыми цифрами". Думаю, такого понятия не существует.
def fill_file(file_name):
    with open(file_name, "w", encoding="UTF-8") as f:
        f.write("".join([str(random.randint(0, 9)) for _ in range(0, 2500)]))


def find_longest_digit(file_name):
    with open(file_name, "r", encoding="UTF-8") as f:
        file_content = f.read()
    max_sequence = ""
    for i in range(0, 10):
        digit_max = max(re.findall(str(i) + "+", file_content))
        if len(digit_max) > len(max_sequence):
            max_sequence = digit_max
    return max_sequence


fill_file("number.txt")
print(find_longest_digit("number.txt"))
