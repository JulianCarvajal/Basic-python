import random


def generar_contrasena():
    mayus = ['A','B','C','D','E','F','G','H','I']
    minus = ['a','b','c','d','e','f','g','h','i']
    simbol = ['!','#','$','&','%','|','/','(',')']
    number= ['1','2','3','4','5','6','7','8','9', '0']

    caracteres = mayus + minus + simbol + number

    contrasena = []

    for i in range(16):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)

    contrasena = "".join(contrasena)
    return contrasena


def run():
    contrasena = generar_contrasena()
    print('Tu nueva contrasena es: ' + contrasena)


if __name__ == "__main__":
    run()