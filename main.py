# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name} y tipo de dato es {type(name)}')  # Press ⌘F8 to toggle the breakpoint.


def greet():
    data = open('data.txt', 'r')
    print(data.read())


def sum_numbers(num1, num2):
    x = num1
    y = num2
    z = x + y
    print(f'EL VALOR DE LA VARIABLE Z ES {z}')
    print(f'DIRECCION DE MEMORIA DE X ES {id(x)} y el tipo de dato es {type(x)}')
    print(f'DIRECCION DE MEMORIA DE Y ES {id(y)} y el tipo de dato es {type(y)}')
    print(f'DIRECCION DE MEMORIA DE Z ES {id(z)} y el tipo de dato es {type(z)}')


def booleans():
    x = True
    y = False
    z = 2 < 1
    print(f'{type(x)}')
    print(f'{type(y)}')
    print(f'{z}')


def cast(num1: str, num2: str):
    print(num1 + num2)
    print(int(num1) + int(num2))


def conditionals(x):
    if x < 4:
        print('El resultado es verdadero')
    else:
        print('El resultado es falso')


def input_console_user():
    value = input("Ingresa tu nombre")
    print(f'Hola {value} eres genial')


def books():
    print('Hola ten un grandioso dia \n necesitamos esta informacion tuya \n')
    author = input("Necesitamos el nombre del  autor: ")
    book = input("Tambien necesitamos el nombre del libro: ")

    print(f' El libro {book} fue escrito por {author}')


def math_operators():
    print('Hola aprendamos matematicas juntos')
    operand_a = input("Necesitamos el primer operando: ")
    operand_b = input("Necesitamos el segundo operando: ")

    num1 = int(operand_a)
    num2 = int(operand_b)

    print(f' la suma es: {num1 + num2} ')
    print(f' la resta es: {num1 - num2} ')
    print(f' la multiplication es: {num1 * num2} ')
    print(f' la division es: {num1 / num2} ')
    print(f' la division entera es: {num1 // num2} ')
    print(f' la potencia es: {num1 ** num2} ')


def area_perimeter_triangle():
    print('Hola aprendamos geometria juntos')
    high = input("Necesitamos la altura del triangulo que mas te guste: ")
    weigh = input("Necesitamos el ancho del triangulo que mas te guste: ")
    area = float(high) * float(weigh)
    perimeter = (float(high) + float(weigh)) * 2

    print(f' el area de tu triangulo es: {area} ')
    print(f' el perimetro de tu triangulo es: {perimeter} ')


def operators_add():
    value = 3
    print(f' valor 1: {value}')
    value += 4
    print(f' valor 2: {value}')
    value -= 1
    print(f' valor 3: {value}')
    value *= 5
    print(f' valor 4: {value}')
    value /= 3
    print(f' valor 5: {value}')
    value //= 5
    print(f' valor 6: {value}')
    validation = value == 56
    print(f' valor es igual a 56 ?: {validation}')
    validation = value != 56
    print(f' valor es diferente a 56 ?: {validation}')
    validation = value <= 56
    print(f' valor es menor igual a 56 ?: {validation}')
    validation = value >= 56
    print(f' valor es mayor igual a 56 ?: {validation}')
    validation = value >= 56 and value <= 56
    print(f' valor en and : {validation}')
    validation = value >= 56 or value <= 56
    print(f' valor en or : {validation}')
    validation = not (value >= 56 or value <= 56)
    print(f' valor en not : {validation}')


def loops():
    count = 0
    while count <= 10:
        print(f' valor contador : {count}')
        count += 1
    else:
        print(' fin while')

    for word in 'holanda':
        if word == 'a':
            print(f'letra encontrada {word}')
            break

    else:
        print(' fin for')

    count = 5
    while count >= 1:
        print(f' valor contador : {count}')
        count -= 1
    else:
        print(' fin while')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    # greet()
    # sum_numbers(4, 5)
    # booleans()
    # cast('1', '2')
    # conditionals(5)
    # input_console_user()
    # books()
    # math_operators()
    # area_perimeter_triangle()
    # operators_add()
    loops()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
