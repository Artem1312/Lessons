class MyClass:
    pass

A = MyClass()
B = MyClass()
C = MyClass()

def hello():
    print("Метод экземпляра - 'hello'")

def hi():
    print("Еще один метод - 'hi'")

A.say = hello
C.say = hi
A.say()

try:
    B.say()
except AttributeError:
    print("Такого метода нет")

C.say()
try:
    MyClass.say()
except AttributeError:
    print("Такой функции нет")

del A.say

try:
    A.say()
except AttributeError:
    print("Такого метода нет")

C.say()
