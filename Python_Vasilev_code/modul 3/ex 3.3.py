def print_text(txt = "Значение аргуента по умолчанию"):
    print(txt)

def show_args(a,b = "Второй аргумент не указан"):
    print(a,b)

def my_func(x="1-й аргумент х", y="второй аргумент у"):
    print(x,y)

print_text("Артгумент указан явно")
print_text()

show_args("Первый аргумент","Второй аргумент")
show_args("Первый аргумент")

my_func()
my_func("Один из аргументов",)
my_func(y="один из аргументов")
