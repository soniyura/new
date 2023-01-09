#Сгенерировать dict() из
# списка ключей ниже по формуле (key : key* key).

keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

b = {}

for index, value in enumerate(keys):
    b[value] = value*value

print(b)
#ожидаемый результат: {1: 1, 2: 4, 3: 9 …}