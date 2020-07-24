# Задача-1:
# Следующая программа написана верно, однако содержит места потенциальных ошибок.
# используя конструкцию try добавьте в код обработку соответствующих исключений.
# Пример.
# Исходная программа:
from typing import Any


def avg(a, b):
    """Вернуть среднее геометрическое чисел 'a' и 'b'.

    Параметры:
        - a, b (int или float).

    Результат:
        - float.
        :rtype:
    """
    return (a * b) ** 0.5


try:
    a = float(input("a = "))
    b = float(input("b = "))
    c = avg(a, b)
    print("Среднее геометрическое = {:.2f}".format(c))
except Exception:
    print("Не правильно указаны значения 'a' или 'b'")


# Задача-2:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import sys
import easy

path_folders = [('dir_' + str(i + 1)) for i in range(9)]

for i in path_folders: 
    easy.creat_folder(i) 


for i in path_folders: 
    easy.delete_folder(i)


# Задача-3:
# Напишите скрипт, отображающий папки текущей директории.

path1 = os.getcwd()
easy.list_folder(path1)


# Задача-4:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

first_file = sys.argv[0]
backup_file = first_file + '.backup'
easy.copy_file(first_file,backup_file)
