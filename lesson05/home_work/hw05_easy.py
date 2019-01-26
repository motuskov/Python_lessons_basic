import os
import stat
import sys
import shutil


# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


# Решение задачи-1
def make_dirs_19():
    for i in range(1, 10):
        try:
            os.mkdir("dir_{}".format(i), stat.S_IWUSR)
            print("Директория dir_{} создана.".format(i))
        except FileExistsError:
            print("Директория dir_{} уже существует.".format(i))


def remove_dirs_19():
    for i in range(1, 10):
        try:
            os.rmdir("dir_{}".format(i))
            print("Директория dir_{} удалена.".format(i))
        except OSError:
            print("Директория dir_{} содержит файлы. Перед удалением очистите директорию.".format(i))


make_dirs_19()
remove_dirs_19()


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


# Решение задачи-2
print(list(filter(os.path.isdir, os.listdir())))


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


# Решение задачи-3, вариант-1 (с использованием shutil)
shutil.copy(sys.argv[0], "{}_".format(sys.argv[0]))


# Решение задачи-3, вариант-2 (копирование содержимого)
def copy_this_file():
    with open(sys.argv[0], "r", encoding="UTF-8") as src:
        with open("{}__".format(sys.argv[0]), "w", encoding="UTF-8") as dst:
            dst.write(src.read())


copy_this_file()
