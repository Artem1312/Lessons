def show(arg):
    try:
        assert arg
        print("Штатный режим")
    except AssertionError as err:
        print("Исключение: ", err.__class__)

show(True)
show(False)
