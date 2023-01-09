# list() колекція типу масива яку можна змінити +/-
# гарантується порядок додається в кінець колекції
print("===========list============")
a = [1, 2, 3, 4]
print(a[0])
a.append(100)
print(a)
a.remove(100)
print(a)

# tuple() колекція типу масива яку не можна змінити
print("===========tuple============")
b = (1, 2, 3)
print(b)

# dict() колекція типу масива зі значеннями
# ключ:значення яку можна змінити +/-
print("===========dict============")
d = {"name": "Petr", "age": 20}
d["ndsvs"] = "sfgdf"
print(d)
print(d["age"])
d["age"] = 21
print(d)
print(d["age"])

#set() колекція типу масива яку  можна змінити підтримує
# унікальні значення але не гарантується порядок
print("===========set============")
s = {1, 2, 3, 4}
print(s)
s.add(10)
print(s)
a = [1, 2, 2, 2, 3] #list
print(set(a)) # робимо set унікальних значень з list
print(list(set(a)))  # з list з неунікальними знач робимо list з
                    # унікальнимим, прокидуємо через set

# int
x = 1
y = 1

# str()
print('=========srt==========')
a = 'dsjvnsdjvn'
print(a[1])
s = a + "_aaaaa"
print(s)

x = 10
print('age: {}'.format(100 + x))




x = 0
if x:
    print(x)
else:
    print("HELLO")