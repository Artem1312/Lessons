class MyClass:
    def set(self,n):
        print("Внимание! Присваивается значение! ")
        self.number = n

    def get(self):
        print("Значение поля: ",self.number)

obj = MyClass()
obj.set(100)
obj.get()
