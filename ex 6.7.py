class MyClass:
    name = "Класс My Class"
    def set(self, n):
        self.nickname = n

    def get(self):
        print("Значение поля: ",self.nickname)
        
    def __init__(self, n):
        self.set(n)
        self.get()

green = MyClass("Зеленый")
print("Принадлежность : ",green.name)

red = MyClass("Красный")
print("Принадлежность : ",red.name)

MyClass.name = "Здесь могла быть ваша реклма "
print("Спрашивает красный ",red.name)
print("Спрашивает зеленый",green.name)
