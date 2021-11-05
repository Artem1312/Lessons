class MyClass:
    name = "Class MyClass"

    def set(self,n):
        self.nickname = n

    def get(self):
        print("Value fild: ",self.nickname)

    def __init__(self,n):
        self.set(n)
        print("Create init class")
        self.get()

green = MyClass("Green")
print("Принадлежность",green.name)
red = MyClass("Red")
print("Принадлежность",red.name)

green.name = "здесь был Зеленый"
print("Спрашвает Красный",red.name)
print("Спрашвает зеленый",green.name)

MyClass.name = "Здесь могла быть Ваша реклама"
print("Спрашвает Красный",red.name)
print("Спрашвает зеленый",green.name)

del green.name
print("Спрашвает зеленый",green.name)

