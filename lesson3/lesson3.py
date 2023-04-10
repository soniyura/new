
#a = 0
#b = [1, 2]

#a = b if a else 'Hello'
#print(a)

#s = 'Hello {}'
#b = s + " world"
#print(id(s), id(b))


#print(s[0])
#d = s.format('world')
#print(d)

#a = [1, 2, 3]
#b = [4, 5, 6]
#a.extend(b)
#print(a)
#print(id(a))

#a, *b, c = (1, 2, None, 4)
#print(a, b, c)
#print(a[:2])
#print(a[2:])
#print(a[2::2])
#print(id(a))

#c = a
#print('c = ', c)
#print(id(a))
#print(id(c))

a = [1, 2, 3, 4]
b = a[:]
#print(b)

#for elem in a:
#     print(elem + 2)

for elem in b:
    if elem == 4:
        continue
    b.pop()
    if elem == 2:
        break

def foo(a):
    a += 1
    return a

a = foo
print(a(10))
b = foo
print(b)
#print(foo(10))


