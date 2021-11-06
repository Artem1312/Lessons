class MyClass:
    def __init__(self,txt):
        self.name = txt

    def __str__(self):
        return self.name

    def __len__(self):
        return len(self.name)

    def __index__(self):
        p = self.name.count(" ")+1
        return p

    def __round__(self):
        self.name = "Сброс значения"
        return self

txt = "Раз, два, три, четыре, пять."
txt += "\nВышел зайчик полулять"
obj = MyClass(txt)
print(obj)
print("количество букв (смволов)",len(obj))
print("Количество слов",obj.__index__())
print("В двоичном коде",bin(obj))
print("В восьмеричном коде",oct(obj))
print("В шеснадцетеричном коде",hex(obj))
print(round(obj))
print(obj)
