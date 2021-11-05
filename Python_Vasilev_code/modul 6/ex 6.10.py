class MyClass:
    def say(self):
        print("Всем привет! ")

obj = MyClass()
obj.say()
MyClass.say(obj)
MyClass.say("Какой-то текст")
