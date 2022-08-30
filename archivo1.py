vocales=['a','e','i','o','u']
espacio=[' ']
palabra=str(input('escribe una palabra para deletrear '))
for i in palabra:
    if i in vocales:
        print(i, 'es una vocal')
    elif i in espacio:
        print('es un espacio')
    else:
        print(i, 'es una consonante')