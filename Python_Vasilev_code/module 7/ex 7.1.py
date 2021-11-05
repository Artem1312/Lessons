class BaseClass:
    name_base = "Класс BaseClass"

    def say_base(self):
        print("Метод say_base()")

class NewClass(BaseClass):
    name_new = "Класс NewClass"

    def say_new(self):
        print("Метод say_new()")

obj_base = BaseClass()
obj_new = NewClass()

print("Класс BaseClass  и экзепляр obj_base:")
print(BaseClass.name_base)

obj_base.say_base()
print("\n Класс NewClass  и экзепляр obj_new:")

obj_new.say_base()
print(NewClass.name_new)
obj_new.say_new()
