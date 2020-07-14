# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

equation = 'y = -12x + 11111140.2121'

x = 2.5
# вычислите и выведите y

equation = 'y = -12x + 11111140.2121'
k = equation[4:7]
b = equation[12:24]
x = 2.5
y = float(k) * x + float(b)
print(y)

# Еще одно решение

equation = 'y = -12x + 11111140.2121'
x = 2.5

print(f'y = {-12 * 2.5 + 11111140.2121}')

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

date = input("Введите дату в формате dd.mm.yyyy")
date_split = date.split('.')
day = int(date_split[0])
month = int(date_split[1])
year = int(date_split[2])

if len(date_split[0]) != 2 or len(date_split[1]) != 2 or len(date_split[2]) != 4:
    print("Не корректный формат даты")
elif day > 31 or day < 1:
    print("Не корректный формат дня")
elif month > 12 or month < 1:
    print("Не корректный формат месяца")
elif year > 9999 or year < 1000:
    print("Не корректный формат года")
else:
    print("Дата введена корректно", date)

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









