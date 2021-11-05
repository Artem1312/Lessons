class MyClass:
    def __init__(self):
        print("Всем привет! ")

    def __del__(self):
        print("Всем пока! ")

print("Проверяем работу деструктора")

obj = MyClass()
print("Экземпляр класса создан. Удаляем его")

del obj
print("ыполнение программы завершено")
