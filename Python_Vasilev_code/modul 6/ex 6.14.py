from copy import copy, deepcopy

class MyClass:
    def __init__(self,name,nums):
        self.name = name
        self.nums = nums

    def show(self):
        print("name ->", self.name)
        print("nums ->", self.nums)

x = MyClass("Python",[1,2,3])
print("Экзепляр x:")
x.show()
y = copy(x)
z = deepcopy(x)
print("Экзепляр y:")
y.show()
print("Экзепляр z:")
z.show()

print("Поле экзепляра х изменяются")

x.name = "Java"
x.nums[0]=0

print("Экзепляр x:")
x.show()
print("Экзепляр y:")
y.show()
print("Экзепляр z:")
z.show()
