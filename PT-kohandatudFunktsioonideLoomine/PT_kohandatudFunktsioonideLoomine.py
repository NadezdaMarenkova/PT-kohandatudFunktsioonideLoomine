from ast import Break
import math
import datetime

# Практическая работа "Создание пользовательских функций"

# 1. Простейшие арифметические операции

"""
Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа, 
третий - операция, которая должна быть произведена над ними. 
Если третий аргумент +, сложить их; если —, то вычесть; * — умножить; / — разделить 
(первое на второе). В остальных случаях вернуть строку "Неизвестная операция".
"""

print("Привет!")

def arithmetic(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        return "Неизвестная операция"

num1 = float(input("\nВведите первое число: "))
num2 = float(input("Введите второе число: "))
operation = input("Введите операцию (+, -, *, /): ")

result = arithmetic(num1, num2, operation)
print(result)

# 2. Високосный год

"""
Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True, если год високосный, и False иначе.
"""

def is_year_leap(year):
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

year = int(input("\nВведите год: "))
if is_year_leap(year):
    print(f"\n{year} год - високосный")
else:
    print(f"\n{year} год - не високосный")


# 3. Квадрат

"""
Написать функцию square, принимающую 1 аргумент — сторону квадрата,  
и возвращающую 3 значения: периметр квадрата, площадь квадрата и диагональ квадрата.
"""

def square(side):
    perimeter = 4 * side
    area = side ** 2
    diagonal = math.sqrt(2) * side
    return perimeter, area, diagonal

side = float(input("\nВведите сторону квадрата: "))

perimeter, area, diagonal = square(side)

print("\nПериметр квадрата: ", perimeter)
print("Площадь квадрата: ", area)
print("Диагональ квадрата: ", diagonal)

# 4. Времена года

"""
Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), 
и возвращающую время года, которому этот месяц принадлежит (talv, kevad, suvi или sügis).
"""

def season(month):
    if month in [12, 1, 2]:
        return "Talv"
    elif month in [3, 4, 5]:
        return "Kevad"
    elif month in [6, 7, 8]:
        return "Suvi"
    elif month in [9, 10, 11]:
        return "Sügis"

month = int(input("\nВведите месяц (1-12): "))
print("Время года : ", season(month))


# 5. Банковский вклад

"""
Пользователь делает вклад в размере a евро сроком на years лет под 10% годовых 
(каждый год размер его вклада увеличивается на 10%. 
Эти деньги прибавляются к сумме вклада, и на них в следующем году тоже будут проценты).
Написать функцию bank, принимающая аргументы a и years, и возвращающую сумму, которая будет на счету пользователя.
"""

def bank(a, years):
    for i in range(years):
        a = a + a * 0.1
        return a

a = float(input("\nВведите размер вклада: "))
years = int(input("Введите срок вклада в годах: "))

result = bank(a, years)
print("Сумма на счету после {} лет: {:.2f} евро".format(years, result))

# 6. Простые числа

"""
Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000, и возвращающую True, если оно простое, и False - иначе.
"""

def is_prime(num):
    if num < 2:
        return False 
    for i in range(2, int(num**(0.5))+1):
        if num % i == 0:
            return False 
        return True

while True:
    num = int(input("\nВведите число от 0 до 1000: ")) 
    if num < 0 or num > 1000:
        print("Ошибка! Введите число от 0 до 1000!")
    else:
        break

if is_prime(num):
    print("Число", num, "является простым")
else:
    print("Число", num, "не является простым")


# 7. Правильная дата

"""
Написать функцию date, принимающую 3 аргумента — день, месяц и год. Вернуть True, если такая дата есть в нашем календаре, и False иначе.
"""


def date(day, month, year):
    try:
        datetime.datetime(year, month, day)
        return True 
    except ValueError:
        return False

day = int(input("\nВведите день: "))
month = int(input("Введите месяц: "))
year = int(input("Введите год: "))

if date(day, month, year):
    print("Такая дата есть в календаре")
else:
    print("Такой даты нет в календаре")



