#Importamos la clases que vamos a utilizar
from paquete_archivos.miarchivo import MiArchivo
from paquete_modelo.mimodelo import Persona, OperacionesPersona
#from paquete_modelo.mimodelo import  ->Otra manera de importar

m = MiArchivo()							#Creamos un objetos m tipo MiArchivo
lista = m.obtener_informacion()			#Declaramos una lista para alamacenar la informacion del objeto m 
lista = [l.split("|") for l in lista]		#Separamos con el split los datos de la lista con el caracter "|""

# print(lista)
lista = lista[1:]  		#Inicializamos la lista en la posicion 1
lista_personas = []		#Declaramos lista_personas como una lista vacia

for d in lista:			#Creamos un for para recorrer la lista
    # print(d)
    p = Persona(d[1], d[2], d[3], d[0], d[4], d[5])         	#Creamos un objeto p tipo Persona y definimos que dato enviamos con su posicion al constructor de la clase Persona 
    lista_personas.append(p)									#Utilizamos el append para ingresar los datos a la lista

operaciones = OperacionesPersona(lista_personas)				#creamos un objeto operaciones tipo OperacionesPersona y enviamos la lista "lista_personas"

print(operaciones.obtener_promedio_n1()) #Presentamos los promedios de las notas 1
print(operaciones.obtener_promedio_n2()) #Presentamos los promedios de las notas 2
print(operaciones.obtener_listado_n1()) #Presentamos las personas con notas1 menores que 15
print(operaciones.obtener_listado_n2()) #Presentamos las personas con notas2 menores que 15
print(operaciones.obtener_listado_personas('R', 'J')) #Presentamos listado de personas que empiecen su nombre con un "R" o "J"