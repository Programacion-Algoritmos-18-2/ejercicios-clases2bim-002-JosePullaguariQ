#Importamos las clases que vamos a utilizar
from paquete_archivos.miarchivo import MiArchivo
from paquete_modelo.mimodelo import Persona

m = MiArchivo()#Creamos un objeto m tipo MiArchivo
lista = m.obtener_informacion() #declaramos una lista para el objeto m
lista = [l.split("|") for l in lista]		#separamos con el split los datos de la lista con el caracter "|""

# print(lista)

lista = lista[1:] #Inicalizamos la lista en la posicion 1
suma_n1 = 0			#Declaramos una variable suma1 para almacenar la suma de las notas1
suma_n2 = 0			#Declaramos una variable suma2 para almacenar la suma de las notas2
# p = Persona(lista[1][1], lista[1][2], lista[1][3], lista[1][0])

for d in lista: #Creamos un for para recorrer la lista
    # print(d)
    #suma_n1 = suma_n1 + int(d[4])
    p = Persona(d[1], d[2], d[3], d[0], d[4], d[5]) #Creamos un objeto p tipo Persona y enviamos los 6 atributos con su posicion al contructor persona
    suma_n1 = suma_n1 + p.obtener_nota1() 			#Sumamos las notas 1
    suma_n2 = suma_n2 + p.obtener_nota2()			#Sumamos las notas 2
    
    if(p.obtener_nota1() < 15 or p.obtener_nota2() < 15): 	#Preguntamos si la nota 1 y nota 2 son menores que 15 presente el nombre de la persona
    	print(p.obtener_nombre())

promedio_n1 = suma_n1/len(lista) 			#Calculamos el promedio de las notas 1
promedio_n2 = suma_n2/len(lista)			#Calculamos el promedio de las notas 2

print(promedio_n1)							#Presentamos el promedio 1 calculado
print(promedio_n2)							#Presentamos el promedio 2 calculado