def test_function():
    a = 'ТЕМА:  "Пространство имен"'

    def inner_function():
        b = 'Я в области видимости функции test_function'
        print(b)
    inner_function()
    return(a)

result = test_function()
print(result)