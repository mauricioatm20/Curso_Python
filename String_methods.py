texto= "Hola Me LLamo Mauricio"

frase= texto
frase1= texto.upper()
frase2= texto.lower()
frase3= texto.split()# lo separa por espacios y lo guarda como una lista
print(frase)
print(frase1)
print(frase2)
print(frase3)


texto= "esto es un texto de mauricio"

frase= texto.replace("mauricio", "todos")
frase1= texto.replace("e" , "a")
print(frase)
print(frase1)

#Une la siguiente lista en un string, separando cada elemento con un espacio.
# Utiliza el método apropiado de listas/strings, y muestra en pantalla el resultado.

lista_palabras = ["La", "legibilidad", "cuenta."]
resultado = " ".join(lista_palabras)
print(resultado)

a= "aprender"
b= "python"
c= "es"
d= "genial"
e= " ".join([a,b,c,d])
print(e)

#Reemplaza en la siguiente frase:
#"Si la implementación es difícil de explicar, puede que sea una mala idea."
#los siguientes pares de palabras:
#"difícil" --> "fácil"
#"mala" --> "buena"
#y muestra en pantalla la frase con ambas palabras modificadas

frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."

# Reemplazar "difícil" por "fácil"
frase_modificada = frase.replace("difícil", "fácil")

# Reemplazar "mala" por "buena"
frase_modificada = frase_modificada.replace("mala", "buena")

print(frase_modificada)
