#String concatenacion
text1 = "Fundamentos con "
text2 = "Python"
result = text1 + text2
print(result)

name = "Andres"
lastName = "Rodriguez"
fullName = name + " " + lastName
print(fullName)

# formato de cadenas
price=97
text3 = f"The price is {price:.2f} dollars"# agregamos decimales al numero entero con .2f
print(text3)

#multiplicacion
text4 = f"La multiplicacion es {20 * 59} "
print(text4)

#funcion Capitalizada
text5 = "python es un lenguaje de alto nivel de program"
result1 = text5.capitalize()
print(result1)
#funcion casefold()  --

#funcion center()
fruit = "banana"
textCenter = fruit.center (40, "♫")
print(textCenter)

#string count()
title1 = "I love apples , apple are my favorite fruit"
result2 = title1.count("apple") #contar caracteres o palabras iguales
print(f"se encontraron {result2} similares")

#string endswith
texto6 = "Curso, fundamentos con Python."
result3 = texto6.endswith(".") #comprueba si dentro de la cadena hay un signo de puntiacion para saber que termina la cadena
print(result3)

#String expandtabs
letter = "F\tU\tP"
letterSpaces = letter.expandtabs(3)#dice cunatos espacios tabular
print(letterSpaces)

#string find
text7 = "Hola, bienvenidos a Colombia."
result4 = text7.find("bienvenidos")
print(f"Se encuentra a partir del caracter: {result4}")

"funcion title" # escribe la primera letra de cada palabra en MAY
result5 = text7.title()
print(result5)

#Funcion isalnum
alphanumeric = "Python321"
result6 = alphanumeric.isalnum()
print(f"{result6},  Si pertenece a los caracteres")

#Funcion isalpha
text8 = "Proyecto X"
result7= text8.isalpha()
print(result7)