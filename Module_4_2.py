# Домашняя работу по уроку "Пространство имен"

def test_function():
    def inner_function():
        print ('Я в области видимости функции "test_function"')
    print(inner_function())

print(inner_function()) # программа выдает ошибку, т.к. функция является вложенной

#    print(inner_function())
          ^^^^^^^^^^^^^^
# NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?

print(test_function()) # returns results