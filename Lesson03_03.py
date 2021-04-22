"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""

# Вариант 1

def max_sum(numb_1, numb_2, numb_3):
    
    print(numb_1 + numb_2 + numb_3 - min(numb_1, numb_2, numb_3))

max_sum(int(input("Введите первое число")), int(input("Введите второе число")), int(input("Введите третье число")))

# Вариант 2

def max_sum(*args):
    numbers_list = [*args]
    numbers_list.sort(reverse=True)
    print(sum(numbers_list[:2]))

max_sum(int(input("Введите первое число")), int(input("Введите второе число")), int(input("Введите третье число")))
