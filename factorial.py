def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

num = int(input('Ingrese un nímero: '))
print(F'El factorial del numero {num} es igual a {factorial(num)}')
