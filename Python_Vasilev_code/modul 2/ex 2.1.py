res = eval(input("Введите что-нибудь: "))
if type(res) == int:
    print("Вы ввели целое число!")
else:
    print("Это точно не целое число!")

print("Работа завершена")
