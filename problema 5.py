'''Una forma de medir la complejidad de un programa es contar su número de líneas de código
(LOC), excluyendo las líneas en blanco y los comentarios. Por ejemplo, un programa como
Del código se observa que este solo tiene dos líneas de código, no cuatro, ya que su primera
línea es un comentario y su segunda línea está en blanco (es decir, solo espacios en blanco).
Esto no es tanto, por lo que es probable que el programa no sea tan complejo.
    Implemente un programa donde se le solicitará al usuario la ruta de un archivo .py (nombre y
ruta). Y retorne la cantidad de líneas de código de ese archivo, excluyendo los comentarios y
líneas en blanco. Si el usuario ingresa una ruta inválida o si el nombre del archivo no termina en
.py, su programa no retornará ningún resultado.
Notas:
- Note que dentro del manejo de errores existe una excepción de tipo
FileNotFoundError la cual le será de mucha utilidad.
- Revise los métodos de cadena
- Dentro del open() el método “readlines” le podría ser de utilidad.
Ejemplo:
- archivo: “hello.py”, número de líneas 2 (Asumiendo que hello.py es el código mostrado
anteriormente)+'''

#C:\Users\TANIA\Desktop\scripts\PC4.py\problema 1.py

import re

def programa_py():
  ruta = str(input("Ingrese la ruta de su archivo: "))
  nomb_arch = str(input("Ingrese el nombre su archivo: "))
  x = re.findall(".py$", nomb_arch)
  while not x:
    print("\nEste no es un archivo python\n")
    nomb_arch = str(input("Ingrese el nombre su archivo: "))
  ruta_arch = ruta + "\\" + nomb_arch
  try:
    open(ruta_arch, 'r')
    return ruta_arch
  except FileNotFoundError:
    print("\nEste archivo no se encuentra\n")
    programa_py()

def contar():
  programa = programa_py()
  print(programa)
  with open(programa, "r") as f:
    version_simple = []
    dentro_doc_string = False
    for linea in f:
        linea = linea.strip()
        if not linea:
            continue
        if linea[0:3] == "'''":
            if linea[-3:] == "'''" and len(linea) != 3:
                pass
            else:
                dentro_doc_string = not dentro_doc_string
            continue
        if linea[0:3] == '"""':
          if linea[-3:] == '"""' and len(linea) != 3:
            pass
          else:
            dentro_doc_string = not dentro_doc_string
          continue
        if dentro_doc_string:
            continue
        if linea[0] == '#':
            continue
        version_simple.append(linea)
  numero = 0
  for lin in version_simple:
    numero += 1
  return print("\nEste archivo de python tiene " + str(numero) + " línea(s) de código\n")

contar()