__author__ = 'Юркова Кристина Сергеевна'

# Задача-1: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользоваться данным ресурсом можно только с 18 лет"

age = int(input("Введите Ваш возраст"))

if age >= 18:
    print("Доступ разрешен")
else:
    print("Извините, пользоваться данным ресурсом можно только с 18 лет")

# Задача-2: Напишите программу, которая спрашивает "Четные или нечетные?", в зависимости от ответа,
# используя цикл с предусловием while или for in
# вывести в одну строку через пробел соотвествующие числа от 0 до 20
# Пример работы:
# $ "Четные или нечетные?"
# четные
# 0 2 4 6 8 10 12 14 16 18 20
# $ "Четные или нечетные?"
# нечетные
# 1 3 5 7 9 11 13 15 17 19
# $ "Четные или нечетные?"
# qwerty (или любая другая строка)
# Я не понимаю, что вы от меня хотите...

a = input("Четные или не четные")
while a == 1:
    break
if a == "нечетные":
    print(1, 3, 5, 7, 9, 11, 13, 15, 17, 19)
    a = 1
elif a == "четные":
    print(0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20)
    a = 1
else:
    print("Я не понимаю, что вы от меня хотите...")

# Задача-3: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

number = input("Введите целое число ")
x = 0
for i in number:
    while int(i) > x:
        x = int(i)
print(x)
