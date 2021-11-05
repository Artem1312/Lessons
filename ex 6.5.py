class MyClass:
    def set(self,n):
        self.num = n

    def get(self):
        print("Значение поля: ",self.num)

    def __init__(self, n=0):
        self.set(n)
        print("Создан экземпляр класса.")
        self.get()

a = MyClass()
b = MyClass(100)
