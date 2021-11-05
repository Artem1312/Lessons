res = eval(input("Введите что-нибудь: "))
resType =  type(res)

if resType == int:
    print("Это целое число! ")
elif resType == float:
    print("Это действительно целове число! ")
else:
    print("Наверно это текст! ")
print("Работа завершена!") 
