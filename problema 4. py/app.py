'''Escriba un programa que realice las siguientes tareas (Puede usar clases y/o funciones,
también puede usar un menú para organizar su programa):
- Solicite un número entero entre 1 y 10 y guarde en un fichero con el nombre
tabla-n.txt la tabla de multiplicar de ese número, donde n es el número introducido.
- Solicite un número entero entre 1 y 10, lea el fichero tabla-n.txt con la tabla de
multiplicar de ese número, donde “n” es el número introducido, y la muestre por
pantalla. Si el fichero no existe debe mostrar un mensaje por pantalla informando de
ello.
- Solicite dos números n y m entre 1 y 10, lea el fichero tabla-n.txt con la tabla de
multiplicar de ese número, y muestre por pantalla la línea m del fichero. Si el fichero
no existe debe mostrar un mensaje por pantalla informando de ello.'''

import ingreso

def opcion1():
    n = int(input('Introduce un número entero entre 1 y 10: '))
    nombre_fichero = 'tabla-' + str(n) + '.txt'
    f = open(nombre_fichero, 'w')
    for i in range(1, 11):
        f.write(str(n) + ' x ' + str(i) + ' = ' + str(n * i) + '\n')
    f.close

def opcion2():
    n =int(input('Introduce un número entero entre 1 y 10: '))
    nombre_fichero = 'tabla-' + str(n) + '.txt'
    try: 
        f = open(nombre_fichero, 'r')
    except FileNotFoundError:
        print('No existe el fichero con la tabla del', n)
    else:
        print(f.read())
        f.close()

def opcion3():
    n =int(input('Introduce un número entero entre 1 y 10: '))
    m= int(input('Introduce otro número entero entre 1 y 10: '))    
    nombre_fichero = 'tabla-' + str(n) + '.txt'
    try: 
        with open(nombre_fichero, 'r') as f:
            lineas = f.readlines()
        print(lineas[m - 1])
    except FileNotFoundError:
        print('No existe el fichero con la tabla del ', n)
        main()

def main():
    opcion=input('''Escribe una opción
    1) opcion 1
    2) opcion 2
    3) opcion 3 
                ''')
    
    if opcion == '1':
            opcion1()
    elif opcion == '2':
            opcion2()
    elif opcion == '3':
            opcion3()
    else:
        print("Comando desconocido, vuelve a intentarlo")
    pass

main()