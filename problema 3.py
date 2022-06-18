'''FIGlet, llamado así por las cartas de Frank, Ian y Glen, es un programa de principios de la
década de 1990 para hacer letras grandes a partir de texto ordinario, una forma de arte ASCII:
- En la siguiente web puede ver una lista de fuentes admitidas por FIGlet
figlet.org/examples.html
- Desde entonces, FIGlet ha sido portado a Python como un módulo llamado pyfiglet.
Cree un programa el cual cumpla con las siguientes especificaciones:
- Solicite al usuario el nombre de una fuente a utilizar. En caso no sé ingrese ninguna
fuente, su programa deberá seleccionar de forma aleatoria la fuente a utilizar.
- Solicite al usuario un texto.
- Finalmente, su programa deberá imprimir el texto solicitado usando la fuente
apropiada.
Notas:
- Instalar la librería usando: pip install pyfiglet
- Para usar la librería, debe hacer:
from pyfiglet import Figlet
figlet = Figlet()
- Puede obtener la lista de fuentes disponibles usando: figlet.getFonts()
- Para seleccionar el fondo a utilizar emplee: figlet.setFont(font=fuente_seleccionada)
- Finalmente podrá imprimir el texto usando : print(figlet.renderText(texto_imprimir))
- Recuerde que random tiene un método random choice '''

import random
from pyfiglet import Figlet
figlet = Figlet()
print(figlet.getFonts())

n=input('El nombre de la fuente a utilizar: ')
if n=='':
    n=random.choice(figlet.getFonts())

figlet.setFont(font = n)
    

texto_imprimir=input('El texto a imprimir: ')

print(figlet.renderText(texto_imprimir))
