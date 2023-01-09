#2) Сгенерировать массив(list()). Из диапазона чисел от 0 до 100
# записать в результирующий массив только четные числа.
from random import sample

a = sample(range(0, 100), 100)
print(a)

b = []
for i in range(len(a)):

    if a[i] % 2 == 0:
        b.append(a[i])

print(b)