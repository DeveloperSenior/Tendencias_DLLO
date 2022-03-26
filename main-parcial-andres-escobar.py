def one():
    valid_pass = 'admin123'
    user_input = input('Ingrese la contraseña bancaria: ')
    if valid_pass == user_input:
        print('La contraseña es la misma')
    else:
        print('La contraseña es incorrecta')


def two():
    weight = input('Ingresa tu peso en Kg: ')
    height = input('Ingresa tu estatura en metros: ')
    imc = round(float(weight) / float(height), 2)
    print(f'Tu índice de masa corporal es {imc}')


def three():
    truth = False
    user_pas = input('Ingresa la contraseña: ')
    while not truth:
        confirm_pass = input('Confirmar contraseña contraseña: ')
        truth = user_pas == confirm_pass
    else:
        print('Las contraseñas coinciden')


def four():
    book_name = input('Ingrese el nombre del libro')
    book_id = input('Ingrese el ID del libro ')
    book_price = input('Ingrese el valor del libro')
    sn = input('El libro es gratis? (S: si, N: n) ')
    truth = 'S' == sn.upper()

    if truth or float(book_price) > 100000:
        print(f'El envio del libro {book_id}-{book_name} es gratis')
    else:
        print('El envio del libro tiene un costo')


if __name__ == '__main__':
    # puntos del parcial
    print('Solucion parcial 1 - Andres Escobar')
    one()
    two()
    three()
    four()
