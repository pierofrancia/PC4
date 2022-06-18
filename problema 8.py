'''Fredrick y tú son buenos amigos. Ayer, Fredrick recibió N tarjetas de crédito de ABCD Bank. Fredrick requiere verificar 
si los números de su tarjeta de crédito son válidos o no. Resulta que eres excelente en expresiones regulares, 
¡así que él está pidiendo tu ayuda!

Una tarjeta de crédito válida de ABCD Bank tiene las siguientes características:

Los números de tarjetas deben iniciar con 4, 5 o 6
La cantidad de dígitos deben ser 16
Deben ser digitos entre [0 - 9]
Puede tener dígitos en grupos de 4, separados por un guión "-".
No debe contener ningún otro separador como ' ' , '_', etc.
No debe tener 4 o más dígitos repetidos consecutivos.'''
import re

tarjeta= '4563-4564-8536-8569'
regex = "[4-6][0-9]{3}.?-[0-9]{4}.?-[0-9]{4}.?-[0-9]{4}$"

print(re.findall(regex, tarjeta))