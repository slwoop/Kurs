# Задача-1:
# Следующая программа написана верно, однако содержит места потенциальных ошибок.
# используя конструкцию try добавьте в код обработку соответствующих исключений.
# Пример.
# Исходная программа:
def avg(a, b):
    """Вернуть среднее геометрическое чисел 'a' и 'b'.

    Параметры:
        - a, b (int или float).

    Результат:
        - float.
    """
    return (a * b) ** 0.5


#a = float(input("a = "))
#b = float(input("b = "))
#c = avg(a, b)
#print("Среднее геометрическое = {:.2f}".format(c))

# Задача-2:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py


import os
import easy

exitos = "a"
while exitos != "0":
    print("1. Перейти в папку")
    print("2. Просмотреть содержимое текущей папки")
    print("3. Удалить папку")
    print("4. Создать папку")
    print("Для выхода выберете 0")
    exitos = input("Выбрать: ")
    print(exitos)
    if exitos == "1":
        dir_name = input("Введите полный путь папки: ")
        easy.change_dir(dir_name)
    elif exitos == "2":
        dir_name = os.getcwd()
        easy.list_folder(dir_name)
    elif exitos == "3":
        dir_name = input("Введите полный путь папки: ")
        easy.delete_folder(dir_name)
    elif exitos == "4":
        dir_name = input("Введите полный путь папки: ")
        easy.creat_folder(dir_name)
    elif exitos == "0":
        pass    
    else:
        print("Такого пункта нет в меню")

          








    
    