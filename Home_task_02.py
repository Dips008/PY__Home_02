# Напишите программу, которая принимает на вход число N и
# выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
import math
n = int(input('Enter an integer n = '))

# def factorials(num):
#     fact = 1
#     for i in range(1, num + 1):
#         fact *= i
#     return fact


array = []
for i in range(1, n+1):
    array.append(math.factorial(i))
print('N = ', n, ' -> ', array)
