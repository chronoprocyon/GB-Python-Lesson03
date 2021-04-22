"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""

def  list_sum(new_list):
    for i in range(len(new_list)):
        try:
            new_list[i] = float(new_list[i])
        except ValueError:
            print("Вы ввели не число")
            return
    global total
    total = total + sum(new_list)
    print(total)


total = 0

while True:
    new_list = input(f"Введите числа, разделенные пробелом. Для прекращения ввода введите '$' отдельно или в конце строки. ").split()
    try:
        sym_index = new_list.index("$")
        new_list = new_list[:sym_index]
        list_sum(new_list)
        break
    except ValueError:
        list_sum(new_list)