vocales=['a','e','i','o','u']
palabra=str(input('escribe una palabra para deletrear '))
for i in palabra:
    if i in vocales:
        print(i, 'es una vocal')
    else:
        print(i, 'es una consonante')