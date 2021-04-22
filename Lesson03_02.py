"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""

def user_info(name, surname, bday, city, email, pnumber):
    print(f"Ваши данные: Имя - {name}, Фамилия - {surname}, Год рождения - {bday}, Город проживания {city}, Email - {email}, Телефон - {pnumber}")

input_name = input("Введите своё имя ")
input_surname = input("Введите свою фамилию ")
input_bday = input("Введите дату рождения ")
input_city = input("Введите город проживания ")
input_email = input("Введите свой email ")
input_pnumber = input("Введите свой номер телефона ")

user_info(name=input_name, surname=input_surname, bday=input_bday, city=input_city, email=input_email, pnumber=input_pnumber)
