class BaseClass:
    name = "Поле name"

    def say(self):
        print("Метод say()")

class NewClass(BaseClass):
    pass

obj = NewClass()
print(NewClass.name)
obj.say()

def hello(self):
    print("Новый метод hello()")

BaseClass.say = hello
BaseClass.name = "Новое значение поля name"

print(NewClass.name)
obj.say()
