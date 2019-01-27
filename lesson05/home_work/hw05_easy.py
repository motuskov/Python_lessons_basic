import os
import stat
import sys
import shutil


# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


# Решение задачи-1
def make_dir(dir_name):
    """
    Функция создает новую директорию в текущей директории.
    :param dir_name: имя директории
    :return: результат операции
    """
    try:
        os.mkdir(dir_name, stat.S_IWUSR)
        return f"Директория {dir_name} успешно создана."
    except FileExistsError:
        return f"Невозможно создать директорию {dir_name}. Директория уже существует."


def remove_dir(dir_name):
    """
    Функция удаляет директорию из текущей директории.
    :param dir_name: имя директории
    :return: результат операции
    """
    try:
        os.rmdir(dir_name)
        return f"Директория {dir_name} успешно удалена."
    except OSError:
        return f"Невозможно удалить директорию {dir_name}."


if __name__ == "__main__":
    for i in range(1, 10):
        print(make_dir(f"dir_{i}"))
    for i in range(1, 10):
        print(remove_dir(f"dir_{i}"))


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


# Решение задачи-2
def show_dirs():
    """
    Функция возвращает список директорий, находящихся в текущей директории
    :return: список директорий
    """
    return list(filter(os.path.isdir, os.listdir()))


if __name__ == "__main__":
    print(show_dirs())


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


# Решение задачи-3, вариант-1 (с использованием shutil)
if __name__ == "__main__":
    shutil.copy(sys.argv[0], "{}_".format(sys.argv[0]))


# Решение задачи-3, вариант-2 (копирование содержимого)
def copy_this_file():
    """
    Функция выполняет копирование данного файла.
    """
    with open(sys.argv[0], "r", encoding="UTF-8") as src:
        with open("{}__".format(sys.argv[0]), "w", encoding="UTF-8") as dst:
            dst.write(src.read())


if __name__ == "__main__":
    copy_this_file()
