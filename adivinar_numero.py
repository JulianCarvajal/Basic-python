import random


def run():
    numero_aleatorio = random.randint(1, 101)
    numero_elegido = int(input('Escribe un número entre 1 y 100: '))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print('Busca un numero mas grande')
            numero_elegido = int(input('Escribe otro número: '))
        else:
            print('Busca un numero mas pequeno')
            numero_elegido = int(input('Escribe otro número: '))
    print('Ganaste!!!')


if __name__ == "__main__":
    run()