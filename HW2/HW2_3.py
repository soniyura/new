#3) Найти общие ключи в двух словарях:
dict_one = { "a": 1, "b": 2, "c": 3,  "d": 4 }

dict_two = { "a": 6,  "b": 7, "z": 20, "x": 40 }

for key in dict_one:
    if key in dict_two:
        print(key, dict_one[key])
        print(key, dict_two[key])


