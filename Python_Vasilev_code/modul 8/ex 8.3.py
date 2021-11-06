def show_me(first,second,*other):
    print("Первый аргумент:",first)
    print("Второй агрумент:",second)
    n = len(other)
    print("Еще осталиось",n,"аргумента:")
    print(other)

show_me(10,20,30,40,50)
