class MyClass:
    def __setattr__(self,attr,val):
        print("Выполняется метод __setattr__()")
        txt="*\tПолю "+str(attr)
        txt+="присваивается значение "+str(val)
        print(txt)
        self.__dict__[attr]=val
        print("")

    def __getattribute__(self,attr):
        print("Выполняется метод __getattribute__()")
        txt="Считывается значение поля "+str(attr)
        print(txt)

        try:
            res = object.__getattribute__(self,attr)
        except AttributeError:
            res = "У экземпляра поля"+str(attr)+"нет"
        print("Метод __getattribute__() завершает работу")
        return res

    def __delattr__(self,attr):
        print("Выполняется метод __delattr__()")
        txt="*\nУдаляется поле "+str(attr)
        print(txt)
        try:
            del self.__dict__[attr]
        except KeyError:
            print(""+str(attr))
        print("Метод __delattr__() выполнен")

obj = MyClass()
obj.name = "Python"
print("Значение поля name:",obj.name)
del obj.name
print(obj.name)
del obj.name
        
