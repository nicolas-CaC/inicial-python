a = []

a.append(1)
print(a)

var1 = 'string'
a.append(var1)
print(a)

b = [True, 'Holas']
a.extend(b)
print(a)

a.insert(1,b)
print(a)

a.pop()
print(a)

a.remove('string')
print(a)

del a[1]
print(a)

a[1] = 123
print(a)

a.extend([1,2,3,2,1,54,5])
print(a)

result = a.index(54)
# print('indice:',result)
print(a[7])

print(a[:7])
print(len(a))
print(54 in a)

d=['a','b','c']
nueva = a + d
print(nueva)

print(a.count(54))
a.sort()
print(a)
a.sort(reverse=True)
print(a)

