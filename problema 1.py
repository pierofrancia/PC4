"""Realizar el juego de “adivina el número”. Para estos deberemos
● Se solicitará un número entero positivo “n” al usuario el cual será el nivel del juego.
(Volver a solicitar en caso ingrese un valor distinto)
● Se generará un número entero aleatorio entre 1 y n el cual no será mostrado. (Emplear
random)
● Solicite al usuario que adivine ese número entero. (Si valor ingresado no es un número
entero, volver a consultar al usuario)
➢ Si el num_ingresado < numero_adividar el programa debe dar como resultado
¡Demasiado pequeño! y pregunte al usuario de nuevo.
➢ Si el num_ingresado > numero_adividar el programa debe dar como resultado
¡Te pasaste! y pregunte al usuario de nuevo.
➢ Si el num_ingresado = numero_adividar el programa debe dar como resultado
¡Adivinaste! y salir del programa.
Ejemplo: Suponiendo que, numero_adivinar =3
Level: 10
Guess: 5
¡Te pasaste!
Guess: 3
¡Adivinaste!                  """


from pickletools import read_uint1
import random

def get_int(msg: str='Ingrese un número entero: ')->int:
        try:
            x = int(input(msg))
            return x
        except:
            return get_int(msg)
       
def ran():
    x=get_int()
    numero=random.randint(1,x)

    def main():
        y=get_int('Adivine el numero entero: ')
        if y<numero:
            print('¡Demasiado pequeño!')
            return main()   
        elif y>numero:
            print('¡Te pasaste!')
            return main()     
        elif y==numero:
            print('¡Adivinaste!')
            pass
    main()

ran()
    