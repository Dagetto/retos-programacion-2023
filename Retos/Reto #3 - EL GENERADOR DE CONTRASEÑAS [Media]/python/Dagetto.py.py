'''/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */'''

import random
import string 

caracteres = list(string.ascii_letters + string.digits + "!@#$%^&*()")


def generador_de_contraseñas ():
    longitud_contraseña = 10

    random.shuffle(caracteres)

    contraseña = []

    for i in range(longitud_contraseña):
        contraseña.append(random.choice(caracteres))

    random.shuffle(contraseña)

    contraseña = "".join(contraseña)
    print(contraseña)


generador_de_contraseñas()