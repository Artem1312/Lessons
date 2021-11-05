txt = "Мы изучаем " "Python"
print(txt)
print("Всего",len(txt),"букв")
print("Индекс \t Буква")
for i in range(len(txt)):
    print(str(i)+": \t"+txt[i])
print(txt[11:])
print(txt[::-1])
word = "Java"
txt = txt[:3]+"не"+txt[2:11]+word
print(txt)

print()
print("**** ex 5.13 ****")
print()

txt = "Мы изучаем PYTHON"
print(txt.upper())
print(txt.lower())
print(txt.capitalize())
print(txt.title())
print(txt.swapcase())
print(txt)

print()
print("**** ex 5.14 ****")
print()

txt = """И.В.Гете. "Фауст" (Орывок):
Бессодержательную речь
Всегда легко в слова облечь.
Из голых слов, ярясь и споря,
Возводя здания теорий.
Словами вера лишь жива.
Как можно отрицать слова?"""
word="слов"
print(txt,end='\n\n')
print("Подстрока встречается ",txt.count(word),"раза")
print("Первая позиция: ",txt.index(word))
print("Следующая позиция: ",txt.find(word,69))
print("Последняя позиция:",txt.rindex(word))
print("В начале инициалы: ",txt.startswith("И.В."))
print("В конце знак вопроса: ",txt.endswith("?"),end='\n\n')
print(txt.replace(" ","_"))

print()
print("**** ex 5.15 ****")
print()

print("123".isdigit(),"12.3".isdigit())
print("abc".isalpha(),"abc123".isalpha())
print("abc12".isalnum(),"ab12\n".isalnum())
print("ABC".isupper(),"aBc".isupper())
print("abc".islower(),"aBc".islower())
print("Ab12 Ab12".istitle(),"Ab12 AB12".istitle())

print()
print("**** ex 5.16 ****")
print()

txt = "_*_ABC_*_abc_*_"
print(txt.lstrip("_*_"))
print(txt.rstrip("_*_"))
print(txt.strip("_*_"))
print(txt.split("*"))
print(txt.rsplit("*"))
print(txt.partition("*"))
print(txt.rpartition("*"))
print("abc \n ABC \n ***".splitlines())
print("_*_".join(["AAA","BBB","CCC"]))

print()
print("**** ex 5.17 ****")
print()

txt = "ABCDEFGH"
print("*"+txt.center(20)+"*")
print("*"+txt.rjust(20)+"*")
print("*"+txt.ljust(20)+"*")

print()
print("**** ex 5.18 ****")
print()

txt = "{0}жды {0} - будет {1}"
print(txt.format("два","четыре"))
print(txt.format("три","девять"))
print("Текст '{0}': {0:<20}.".format("abcdef"))
print("Текст '{0}': {0:^20}.".format("abcdef"))
print("Текст '{0}': {0:>20}.".format("abcdef"))
