# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from time import sleep


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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    greet()
    sum_numbers(4, 5)
    booleans()
    cast('1', '2')
    conditionals(5)
    input_console_user()
    books()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
