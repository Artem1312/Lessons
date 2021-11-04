print("Сумма натуральных чисел")
n = 100
text = "1+2+...+"+str(n)+" = "
i = 1
s = 0
while i <= n:
    s = s+i
    i = i+1

print(text, s)


print()
print("**** ex 2.5 ****")
print()

print("Сумма натуральных чисел")
n = 100
text = "1+2+...+"+str(n)+" = "
i = 1
s = 0

while True:
    s+=i
    i+=1
    if i>n:
        break
print(text,s)


print()
print("**** ex 2.6 ****")
print()


n = 500
dz = 1/n;
pts = 0
i = 0
while i <= n:
    x = dz*i
    j = 0
    while j <= n:
        y = dz*j
        if y <= x and y >= x**2:
            pts = pts+1
        j=j+1
    i=i+1
s = pts/(n+1)**2
print("Площадь фигуры: ",s)


print()
print("**** ex 2.7 ****")
print()


print("Сумма натуральных чисел")
n=100
text = "1+2+...+"+str(n)+" = "
s = 0
for i in range(1,n+1):
    s=s+i
print(text,s)    
    


print()
print("**** ex 2.8 ****")
print()


txt = "Python"
i=1
for s in txt:
    t = str(i)+"я буква: "
    print(t,s)
    i = i+1
print("Работа программы завершена")
    


print()
print("**** ex 2.9 ****")
print()

print("Проверяем содержимое списка")
#myList = [1,3+2j, True, 4.0]
myList = [1,3+2j, "Python", 4.0]

print("Список: ",myList)
for s in myList:
    if type(s) == str:
        print("В списке есть текстовые элементы")
        break
    else:
        print("В списке нет текстовых элементов")
print("Проверка закончена")



print()
print("**** ex 2.10 ****")
print()

print("Поиск совпадающих элементов")
A = [2, False, 9.1, 2-1j, "hello", 5, "Python"]
B = [5, 3, "HELLO", 7, 12.5, "Python", True, False]
print("1-й список: ",A)
print("2-й список: ",B)
print("Совпадают: ")
i = 0
for a in A:
    i = i+1
    j = 0
    for b in B:
        j = j+1
        if a == b:
            txt = str(i)+"-й элемент из 1-го списка и "
            txt = txt + str(j)+"-й элемент из 2-го списка"
            print(txt)
print("Поиск закончен.")


print()
print("**** ex 2.11 ****")
print()


print("Решаем уравнение ax = b ")

try:
    a = float(input("Введите а: "))
    b = float(input("Введите b: "))
    x = b/a
    print("Решение уравнения: х= ",x)
except:
    print("Вы ввели неккоректные данные! ")
print("Спасибо работа завершена!")


print()
print("**** ex 2.11 ****")
print()

print("Решаем уравнение ax = b ")
try:
    a = float(input("Введите а: "))
    b = float(input("Введите b: "))
    x = b/a
    print("Решение уравнения: х= ",x)
except ValueError:
    print("Нужно было ввести число! ")
except ZeroDivisionError:
    print("Внимание! На коль делить нельзя")
print("Спасибо работа завершена!")    
