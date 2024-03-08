#Definir una clase estudiante, crear varios estudiantes y meterlos en una lista

class Estudiante:

    # __init__: Este método se utiliza para inicializar los atributos de la instancia.
    # def __init__(slef,nombre,edad): #self y this(en Java) se utilizan para referirse al objeto actual dentro de los métodos de la clase

    def __init__(this,nombre,edad):
        this.nombre= nombre
        this.edad= edad

estudiante1 =  Estudiante("ana" , 39)
estudiante2 =  Estudiante("manuel" , 42)

#guardar los estudiantes en una lista
lista_estudiantes = [estudiante1,estudiante2]

#recorrer la lista y guarda los estudiantes en estudiante.
for estudiante in lista_estudiantes:
    print("nombre:" , estudiante.nombre,"/", "edad:" ,estudiante.edad)
