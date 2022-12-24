# Задайте список из N элементов, заполненных числами из
# промежутка [-N, N]. Найдите произведение элементов на
# указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
import random

n = int(input('Enter an integer n = '))
res = []
for i in range(n):
    res.append(random.randint(-n, n+1))
print(res)

with open("file.txt") as f:
    lst = [int(x) for x in f.read().split()]
print(lst)

comp = 1

for i in range(0, len(lst)):
    comp *= res[lst[i]]

print(res, lst, ' -> ', comp)
