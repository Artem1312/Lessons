a = 70>>3
b = ~a
c = a<<1

print(a,b,c)
print(7|3,7&3,7^3)


print ('**************************')


a = True
b = not a
print(a,b)
c = a and b
d = a or b
print(c,d)

print ('**************************')

x = 10
y = 20
z = x and y
print(z)
z = x or y
print(z)
print(not x)

print ('**************************')

a = 100
b = 200
print(a<b,a>=b,a==100,b!=199)

print ('**************************')

a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
value_1 = "Первое число больше второго"
value_2 = "Второе число не меньше первого"

res = value_1 if a>b else value_2
print(res)

print ('**************************')
