# значення тапл використовються як ключі для dict
tupleKey = ('Name', 'Age', 'Time')
tupleValue = ('Jone', 23, '14:30')

#print(tuple)

dict = {tupleKey[0]: tupleValue[0],
        tupleKey[1]: tupleValue[1],
        tupleKey[2]: tupleValue[2]}

#print(dict)
#print(dict.get(tuple[0]))
#print(dict.get(tuple[1]))
#print(dict.get(tuple[2]))

for key, value in dict.items():
        print(key, "-", value)



