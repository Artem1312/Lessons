print("**** ex 4.1 ****")
print()

s = [10,20,30]

s.append([1,2])
print(s)

s.extend([3,4])
print(s)

print()
print("**** ex 4.2 ****")
print()

s = [10,20,30]
s.insert(1,-5)
print(s)
s.insert(1,[1,2])
print(s)
s[2:2]=[3,4]
print(s)
s[2:3]=[100,200]
print(s)


print()
print("**** ex 4.3 ****")
print()

s = [i*(10-i) for i in range(11)]
print(s)

print("Удаляем элемент", s.pop(5))
print(s)

s.remove(21)
print(s)

del s[3]
print(s)

s[2:5]=[]
print(s)

s[1:3]=[-1,-2,-3,-4,-5]
print(s)


print()
print("**** ex 4.4 ****")
print()

a = [10,20,30]
print("Список a",a)
b = a
c = a[:]
d = a.copy()
print("Список b",b)
print("Список c",c)
print("Список d",d)
print("Меняем значение элемента a[1]=0.")
a[1]=0

print("Список a",a)
print("Список b",b)
print("Список c",c)
print("Список d",d)



print()
print("**** ex 4.5 ****")
print()


x = [10,20,[100,200],30,[300,400]]
y = x[:]
z = x.copy()
print("Список x",x)
print("Список y",y)
print("Список z",z)
print("Меняем элементы: x[2][1]=0 и x[4]=0.")
x[2][1]=0
x[4]=0
print("Список x",x)
print("Список y",y)
print("Список z",z)



print()
print("**** ex 4.6 ****")
print()

import copy

A = [[10,20],[30,40],[50,60]]
B = copy.deepcopy(A)

print("Список A",A)
print("Список B",B)

print("Выполняется командв A[0][1]=0 и A[1][1][1]=0")
A[0][1] = 0
#B[1][1][1] = 0

print("Список A",A)
print("Список B",B)




