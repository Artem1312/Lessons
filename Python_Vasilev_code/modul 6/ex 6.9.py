class MyClass:
    pass

A = MyClass()
B = MyClass()

A.first = "Экзепляр класса А"
B.second = "Экзепляр класса В"

MyClass.total = "Класс MyClass"
print(A.total,"->",A.first)

try:
    print(A.second)
except AttributeError:
    print("Такого экзепляра у класса А нет")

print(B.total,"->",B.second)

try:
    print(B.first)
except AttributeError:
    print("Такого экзепляра у класса B нет")

del MyClass.total

try:
    print(A.total)
except AttributeError:
    print("Такого поля нет")

try:
    print(B.total)
except AttributeError:
    print("Такого поля нет")

del A.first

try:
    print(A.first)
except AttributeError:
    print("Такого экзепляра у класса А нет")
    
    
