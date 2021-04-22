"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""

def dev_func(divident, divider):
    if divider == 0:
        print("Нельзя делить на 0")
    else:
        print(dev_func(divident, divider))



divident_in = float(input("Введите делимое: "))
divider_in = float(input("Введите делитель: "))


dev_func(divident_in, divider_in)
