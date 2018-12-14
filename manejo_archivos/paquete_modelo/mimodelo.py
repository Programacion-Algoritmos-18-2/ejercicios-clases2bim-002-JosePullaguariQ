"""
    creación de clases
"""
class Persona(object):#Creamos la clase persona 
    """
    """   
    def __init__(self, n, ape, ed, cod ,n1, n2):#Contructor de la clase persona que recibe 6 atributos del archivo demo_notas
        """
        """
        self.nombre = n
        self.edad = int(ed)
        self.codigo = int(cod)
        self.apellido = ape
        self.nota1 = int(n1)
        self.nota2 = int(n2)

    #Metodos de agregar y obtener para los atributos de la clase
    def agregar_nombre(self, n):#Metodo para agregar nombre
        """
        """
        self.nombre = n

    def obtener_nombre(self):#Metodo para obtener nombre
        """
        """
        return self.nombre

    def agregar_edad(self, n):#Metodo para agregar edad
        """
        """
        self.edad = int(n)

    def obtener_edad(self):#Metodo para obtener edad
        """
        """
        return self.edad
    
    def agregar_codigo(self, n):#Metodo para agregar codigo
        """
        """
        self.codigo = int(n)

    def obtener_codigo(self):#Metodo para obtener codigo
        """
        """
        return self.codigo
    
    def agregar_apellido(self, n):#Metodo para agregar apellido
        """
        """
        self.apellido = n

    def obtener_apellido(self):#Metodo para obtener apellido
        """
        """
        return self.apellido

    def agregar_nota1(self, n):#Metodo para agregar nota 1
        """
        """
        self.nota1 = int(n)

    def obtener_nota1(self):#Metodo para obtener nota 1
        """
        """
        return self.nota1

    def agregar_nota2(self, n):#Metodo para agregar nota 2
        """
        """
        self.nota2 = int(n)

    def obtener_nota2(self):  #Metodo para obtener nota 2
        """
        """
        return self.nota2
    
    #Metodo str para presentar los datos 
    def __str__(self):
        """
        """
        #Imprimimos los atributos
        return "%s - %s - %d - %d - %d - %d" % (self.nombre, self.apellido,\
                self.edad, self.codigo, self.nota1, self.nota2)


class OperacionesPersona(object):#Creamos la clase Operaciones Persona para hacer todas los procesos
    """
    """
    def __init__(self, listado):#Constructor de la clase
        """
        """
        self.listado_personas = listado

    def obtener_promedio_n1(self):#Metodo para calcular el promedio de las notas 1
        suma = 0                            #declaramos una variable para las sumas de notas1
        print("\nPromedio de notas 1")
        for n in self.listado_personas:     #creamos for para recorrer la lista
            suma = suma + n.obtener_nota1() #sumamos las notas 1
        promedio = suma / len(self.listado_personas) #calculamos el promedio de notas 1

        return promedio

    def obtener_promedio_n2(self):#Metodo para calcular el promedio de las notas 2
        suma = 0                            #declaramos una variable para las sumas de notas 2  
        print("\nPromedio de notas 2")
        for n in self.listado_personas:     #creamos un for para recorrer la lista
            suma = suma + n.obtener_nota2() #sumamos las notas2
        promedio = suma / len(self.listado_personas) #calculamos el promedio de notas 2
        
        return promedio
    
    def obtener_listado_n1(self):#Metodo para calcular las personas que tengan la nota1 inferior a 15
        cadena = " "                                    #concatenamos la cadena
        print("\nListado de personas con nota 1 menor que 15")
        for n in self.listado_personas:                 #creamos for para recorrer el lista
            if(n.obtener_nota1() < 15):                 #preguntamos si la nota 1 es menor que 15
                cadena = "%s%s - Nota: %d" % (cadena, n.obtener_nombre(), n.obtener_nota1())
        return cadena

    def obtener_listado_n2(self):#Metodo para calcular las personas que tengan la nota2 inferior a 15
        cadena = " "                                    #Concatenamos la cadea
        print("\nListado de personas con nota 2 menor que 15")
        for n in self.listado_personas:                 #creamos for para recorrer el lista
            if(n.obtener_nota2() < 15):                 #preguntamos si la nota es menor que 15
                cadena = "%s%s - Nota: %d" % (cadena, n.obtener_nombre(), n.obtener_nota2())#almacenamos a la cadena  el nombre y la nota 2
        return cadena                                   #Retornamos la cadena

    def obtener_listado_personas(self, n1, n2):#Metodo para calcular los nombres de las personas que empiecen con J o con R
        cadena = " "                                    #concatenamos la cadena
        lista = []                                      #declaramos una lista para almacenar los nombres
        print("\nListado de personas que empiezan su nombre con J y R")
        for n in self.listado_personas:                 #creamos for para recorrer el lista
            if(n1 == n.obtener_nombre()[0] or n2 == n.obtener_nombre()[0] ):
                lista = cadena = "%s%s %s\n" % (cadena, n.obtener_nombre(), n.obtener_apellido())#almacenamos a la cadena el nombre y el apellido
        return lista                                    #retornamos la lista

    def __str__(self):#Metodo str para presentar los datos de la clase
        """
        """
        cadena = " "#Concatenamos la cadena
        for n in self.listado_personas: #creamos for para recorrer el lista
            cadena ="%s %s %s\n" % (cadena, n.obtener_nombre(), n.obtener_apellido())#Almacenamos en la cadena con los datos que queremos presentar
        return cadena #retornamos la cadena