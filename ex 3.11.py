x = 100
def test_vars():
    x = "локальная переменная "
    print("В теле функции x = ", x)

test_vars()
print("Вне функции x = ", x)
