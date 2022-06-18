'''Escriba una expresión regular que valide una lista de correos electrónicos del tipo
correo@dominio.com, teniendo en cuenta lo siguiente:
● “correo”:
○ Se permiten los caracteres en mayúscula y minúscula
○ También se permite el empleo de número Números
○ Se permite el uso de caracteres especiales como: !, #, %, &, *, $, .
● Debe contener @
● “Dominio”:
○ Puede ser cualquier conjunto de caracteres
● Solo puede terminar con .com
Ejemplo:
- ENTRADA: ['n.john.smith@gmail.com', '87victory@hotmail.com',
'!#mary-=@msca.net']
- SALIDA:
The email n.john.smith@gmail.com is a valid email
The email 87victory@hotmail.com is a valid email
The email !#mary-=@msca.net is invalid
Nota:
Solo debe generar la crear la expresión regular'''
import re
ENTRADA= ['n.john.smith@gmail.com', '87victory@hotmail.com','!#mary-=@msca.net']

regex = re.compile(r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])")
expresion_regular = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"

print(re.fullmatch(regex,ENTRADA[1]))

def isValid(email):
    if re.fullmatch(regex, email):
        print("Valid email")
    else:
        print("Invalid email")

isValid('n.john.smith@gmail.com')
isValid('87victory@hotmail.com')
isValid('!#mary-=@msca.net')