#Toma cada tercer caracter empezando desde el noveno hasta el final de la frase, e imprime el resultado.

frase = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
extra = frase[8::3]
print(extra)

frase = "Nunca confíes en un ordenador que no puedas lanzar por"
extra = frase[0:9]
print(extra)

#extraer
texto = "ABCDEFGHYJKLM"
fragmento = texto[2:5]
fragmento1 = texto[:5]
fragmento2= texto[2:]
print(fragmento)
print(fragmento1)
print(fragmento2)

#Invierte la posición de todos los caracteres de la siguiente frase y muestra el resultado en pantalla.

frase = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
inver = frase[::-1]
print(inver)