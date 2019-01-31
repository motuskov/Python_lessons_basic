import os
import sys
import re


# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.


# Решение задания-1
def print_help():
    """
    Функция выводит справку по функциям данной программы.
    """
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - создание копии файла")
    print("rm <file_name> - удаление файла")
    print("cd <full_path or relative_path> - изменение текущей директории")
    print("ls - отображение полного пути текущей директории")


def get_cwd():
    """
    Функция возвращает абсолютный путь к текущей директории.
    :return: абсолютный путь к текущей директории
    """
    try:
        with open("hw05_hard_settings.txt", encoding="UTF-8") as settings_file:
            dir_path = settings_file.read()
            return dir_path if os.path.isdir(dir_path) else os.getcwd()
    except OSError:
        return os.getcwd()


def make_dir():
    """
    Функция создает новую директорию в текущей. Имя создаваемой директории берем из аргумента командной строки.
    """
    if not arg:
        print("Необходимо указать имя директории вторым параметром")
        return

    dir_path = os.path.join(get_cwd(), arg)

    try:
        os.mkdir(dir_path)
        print(f"Директория {arg} создана.")
    except FileExistsError:
        print(f"Директория {arg} уже существует.")


def ping():
    """
    Функция выводит текст 'pong'.
    """
    print("pong")


def cp():
    """
    Функция создает копию файла в текущей директории. Имя копируемого файла берем из аргумента командной строки.
    """
    if not arg:
        print("Необходимо указать имя файла вторым параметром")
        return

    file_path = os.path.join(get_cwd(), arg)

    try:
        with open(file_path, "r", encoding="UTF-8") as src:
            with open(f"{file_path}_copy", "w", encoding="UTF-8") as dst:
                dst.write(src.read())
                print(f"Копия файла {arg} создана.")
    except FileNotFoundError:
        print(f"Файл {arg} не найден.")


def rm():
    """
    Функция удаляет файл в текущей директории. Имя удаляемого файла берем из аргумента командной строки.
    """
    if not arg:
        print("Необходимо указать имя файла вторым параметром.")
        return

    file_path = os.path.join(get_cwd(), arg)

    if input(f"Вы уверены, что вы хотите удалить файл {file_path}? (y/n)") != "y":
        return

    try:
        os.remove(file_path)
        print(f"Файл {arg} успешно удален.")
    except OSError:
        print(f"Невозможно удалить файл {arg}.")


def cd():
    """
    Функция записывает в файл 'hw05_hard_settings.txt' абсолютный путь текущей директории. Имя текущей директории
    берем из аргумента командной строки.
    """
    if not arg:
        print("Необходимо указать имя директории вторым параметром")
        return

    dir_path = arg if re.match(r"\/|[a-zA-Z]\:\\", arg) else os.path.join(get_cwd(), arg)

    if not os.path.isdir(dir_path):
        print("Указанной директории не существует.")
        return

    try:
        with open("hw05_hard_settings.txt", "w", encoding="UTF-8") as settings_file:
            settings_file.write(dir_path)
            print("Текущая директория изменена.")
    except OSError:
        print("Не удалось изменить текущую директорию.")


def ls():
    """
    Функция выводит абсолютный путь текущий директории.
    """
    print(get_cwd())


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": cp,
    "rm": rm,
    "cd": cd,
    "ls": ls
}

try:
    arg = sys.argv[2]
except IndexError:
    arg = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
