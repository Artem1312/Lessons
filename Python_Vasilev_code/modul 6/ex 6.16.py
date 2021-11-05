class MyClass:
    def __init__(self,arg,nums=None):
        if type(arg) == MyClass:
            self.name = arg.name[:]
            self.nums = arg.nums[:]
        else:
            self.name = arg
            self.nums = nums

    def show(self):
        print("name ->",self.name)
        print("nums ->",self.nums)


x = MyClass("Python",[1,2,3])
print("Экзепляр x:")
x.show()

y = MyClass(x)
y.show()

print("Поля экзепляра х изменяются")

x.name = "Java"
x.nums[0] = 0

print("Экзепляр x:")
x.show()

print("Экзепляр y:")
y.show()
