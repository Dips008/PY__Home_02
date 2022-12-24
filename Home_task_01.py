# Напишите программу, которая принимает на вход вещественное
# число и показывает сумму его цифр.
#  Пример:
#  - 6782 -> 23
#  - 0,56 -> 11

# Var_1
# str_number = str(input('Enter a real number = '))
# suma = 0
# for i in str_number:
#     if i.isdigit():
#         suma += int(i)
# print(' - ', str_number, ' -> ', suma)

# Var_2
str_number = str(input('Enter a real number = '))
print(' - ', str_number, ' -> ', end='')
str_number = str_number.replace('.', '')
print(sum(map(int, list(str_number))))
