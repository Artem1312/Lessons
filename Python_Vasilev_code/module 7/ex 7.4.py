class BaseClass:
    def __init__(self,num):
        self.id = num
        
    def get(self):
        print("ID:",self.id)

    def show(self):
        print("Поле экзепляра базового класса")
        self.get()

class NewClass(BaseClass):
    def __init__(self,num,txt):
        super().__init__(num)
        self.name = txt

    def get(self):
        super().get()
        print("Name:",self.name)
        


obj_base = BaseClass(1)
print("Вызываем метод show() из экзепляра obj_base:")
obj_base.show()

obj_new = NewClass(10,"десятка")



print("Вызываем метод show() из экзепляра obj_new:")
obj_new.show()
