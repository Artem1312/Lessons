def F(A):
    class Alpha(A):
        def hi(self):
            print("Class Alpha!")
    return Alpha

def Q(A):
    class Bravo(A):
        def hi(self):
            print("Class Bravo!")
    return Bravo

@F
class First:
    def hello(self):
        print("Class First!")

@F
class Second:
    def hello(self):
        print("Class Second!")

@Q
@F

class Third:
    def hello(self):
        print("Class Third!")

def show_obj(obj):
    print("Класс экзепляра", obj.__class__)
    obj.hi()
    obj.hello()

def show_class(A):
    print("Имя класса", A.__name__)
    print("Базовый класс", A.__bases__)
    print("Цепочка наследования", A.__mro__)

one = First()
two = Second()
three = Third()

print("Экзепляры классов")
for obj in [one,two, three]:
    show_obj(obj)

print("Classes")
for A in [First,Second,Third]:
    show_class(A)
