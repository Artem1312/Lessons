class Alpha:
    def hi():
        print("Class Alpha")

class Bravo:
    def hi():
        print("Class Bravo")

class Charlie:
    def hi():
        print("Class Charlie")

class Delta(Alpha):
    pass

class Echo(Delta):
    pass

class Foxtrot(Bravo, Alpha):
    pass

class Golf(Foxtrot):
    pass

class Hotel(Echo, Charlie, Golf):
    pass

Echo.hi()
Golf.hi()
Hotel.hi()
