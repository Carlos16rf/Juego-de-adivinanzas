# -*- coding: utf-8 -*-
import random


def main():
    numero_secreto = random.randint(1, 100)
    print("¡Bienvenido al juego de adivinanza de números!")
    print("He elegido un número entre 1 y 100. ¡Intenta adivinarlo!")
    
    while True:
        adivinanza = int(input("Introduce tu adivinanza: "))
        if adivinanza < numero_secreto:
            print("Demasiado bajo. Intenta de nuevo.")
        elif adivinanza > numero_secreto:
            print("Demasiado alto. Intenta de nuevo.")
        else:
            print("¡Felicidades! ¡Has adivinado el número!")
            break  # Sal del bucle si la adivinanza es correct
    
if __name__ == "__main__":
    main()
