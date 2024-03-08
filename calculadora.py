class calculadora:
    def suma(self,num1,num2):

        return num1+num2
    def resta(self,num1,num2):
        return num1-num2
    def multiplicacion(self,num1,num2):
        return num1*num2
    def division(self,num1,num2):
        return num1/num2
#vamos a crear dos objetos diferentes de tipo calculadora
cal=calculadora()
cal2=calculadora()

print(id(cal))
print(id(cal2))
cal3= cal2

#el di muestra que son objetos diferentes tenemos dos objetos cal y cal2  pero cal3 es igual que cal2
print(id(cal3))



print("Resultado:", cal.multiplicacion(3,4))
print("Resultado:" , type(cal.multiplicacion(3,4)))

print ("Resultado:", cal.division(9,4))

print("Resultado:", cal.multiplicacion(2,4))
print("Resultado:" , type(cal.multiplicacion(3,4)))

print ("Resultado:", cal.division(40,30))

print ("Resultado:", type(cal.division(9,4)))