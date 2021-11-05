res = eval(input("Введите что-нибудь: "))
resType =  type(res)

if resType == int:
    print("Это целое число! ")
if resType == float:
    print("Это действительно целове число! ")
if resType != int and resType != float:
    print("Наверно это текст! ")
print("Работа завершена!")    
