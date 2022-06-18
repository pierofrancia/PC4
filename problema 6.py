'''Escriba una expresión regular que encuentre todas las coincidencias que sigan el siguiente
patrón. @robot<digito><signo especial>
Use el siguiente texto para la búsqueda de coincidencias.
cadena = '@robot9! @robot4& I have a good feeling that the show is going to be amazing! @robot9$
@robot7%'
Su programa debe dar como resultado los siguientes valores: [“@robot9!”, “@robot4&”, “@robot9$”,
“@robot7%”]'''

import re

cadena = '@robot9! @robot4& I have a good feeling that the show is going to be amazing! @robot9$ @robot7% '
b=r"@robot\d\W"
print(re.findall(b,cadena))
