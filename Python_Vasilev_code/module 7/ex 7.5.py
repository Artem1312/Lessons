class BoxSize:
    def __init__(self,width,heigth,depth):
        self.width = width
        self.heigth = heigth
        self.depth = depth

    def volume(self):
        return self.width*self.heigth*self.depth

    def show(self):
        print("Размер и объем ящика:")
        print("Ширина",self.width)
        print("Высота",self.heigth)
        print("Шлубина",self.depth)
        print("Объем",self.volume())
        
class BoxParams:
    def __init__(self,weight,color):
        self.weight = weight
        self.color = color

    def show(self):
        print("Дополниетельные параметры ящика")
        print("Вес (масса):",self.weight)
        print("Цвет:",self.color)

class Box(BoxSize, BoxParams):
    def __init__(self,width,heigth,depth,weight,color):
        BoxSize.__init__(self,width,heigth,depth)
        BoxParams.__init__(self,weight,color)
        self.show()

    def show(self):
        BoxSize.show(self)
        BoxParams.show(self)

obj = Box(10,20,30,5,"зеленый")
        
