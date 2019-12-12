import pyperclip, os

class Alumno():

    #Esto es una variable de clase,
    ageUpdate = 1

    # La funcion INIT se usa para inicializar el programa. Se pasan argumentos, y por cada uno que se pasa se toma como uno de los argumentos de la clase
    #El primer argumento es SELF, que va siempre, el resto son los que se le pasan al llamarlas
    def __init__(self, name, last, age):
        #Ejemplo, usamos self.XXX, siendo XXX el argumento que estemos pasando. En si es lo mismo usar otro nombre pero se suele usar asi para evitar confusion
        self.name = name
        self.last = last
        self.age = age
        self.email = name + '.' + last + '@escuela.com'

    #Definimos otra funcion. En este caso, la funcion devuelve el nombre completo
    def fullname(self):
        return '{} {}'.format(self.name, self.last)

    #Usamos la variable de clase previamente establecida.
    def actualizarEdad(self):
        self.age = int(self.age + self.ageUpdate)

    def listar(self):
        self.age = str(self.age)
        l2 = []
        val = self.__dict__ #Aca creo un diccionario con los datos de la instancia
        aL = []
        for i in val:
            aL = (val.values())
        for i in aL:
            l2.append(i)
        l2 = ' '.join(l2)
        print(l2)
        ####################################################################
        f = open("al2", "a")
        #x = 2000
        #while x > 0:
            #x -= 1
        f.write(l2 + '\n')
        f.close()
#Creamos una clase heredada. Asi, la clase Maestros esta heredando a la clase Alumno.
#Si se deja vacia, o con "pass", toma todos los datos de la clase Alumno y funciona igual
class Maestros(Alumno):
    #Cambiamos la variable de clase de Alumno, ahora, al agregar una instancia usando Maestro como clase, tomara esta en lugar de la de la clase padre
    ageUpdate = 32

    #Inicializamos de igual manera que antes la clase, con la funcion __init__
    #vemos que se le pasan los mismo parametros, solo que se le agrega uno mas (en este caso el grado)
    #la sentencia de abajo (super().__init__() lo que hace es indicarle a la clase Maestro que la clase padre (Alumno) se va a ocupar de los argumentos name last y age.
    #De esta forma, la clase Maestro es la que se va a encargar solo del nuevo argumento, en este caso grado
    #Se pasa como parametros en la funcion SUPER los argumentos que manejara la clase padre, o sea Alumno
    def __init__(self, name, last, age, grado ):
        super().__init__(name, last, age)
        self.grado = grado

class Directores(Alumno):

    def __init__(self, name, last, age, empleados=None ):
        super().__init__(name, last, age)
        if self.empleados is None:
            self.empleados = []
        else:
            self.empleados = empleados

    def add_emp(self, emp):
        if emp not in self.empleados:
            self.empleados.append(emp)
    def rem_emp(self, emp):
        if emp in self.empleados:
            self.empleados.remove(emp)

    def print_emp(self):
        for emp in self.empleados:
            print('-->' , emp.fullname() )


a1 = Maestros('Pedro', 'Sanchez', 12, "6to")
a2 = Maestros('Juana', 'Roble', 10, "3ro")
a3 = Maestros('Paula', 'Robbie', 11, "2do")


dire1 = Directores('Aurora', 'Gomez', 75, [a1])

print(dire1.last)

























""""
print(a1.grado)

print(a1.age)
a1.actualizarEdad()
print(a1.age)
"""
""
# Aca se llama a la funcion. Cuando se hace, se pasa la funcion y se asignan los valores que indica la definicion de __init__
# Al hacer esto, se crea una instancia de la clase.
"""
a1 = Alumno('Pedro', 'Sanchez', "12")
a2 = Alumno('Juana', 'Roble', "10")
a3 = Alumno('Nicolas', 'Muñoz', "9")
Alumno.listar(a1)
a2.listar()
a3.listar()
"""
"""
print(a1.age)
a1.actualizarEdad()
print(a1.age)
print(Alumno.ageUpdate)
print(a1.__dict__)

l2 = []
val = a1.__dict__
a1L = []
for i in val:
    a1L = (val.values())
for i in a1L:
    l2.append(i)
#l2 = ' '.join(str(l2))
#print(l2)
l2 = ' '.join(l2)
print(l2)

f = open("alumnos.txt", "a")
f.write(l2)
f.close()
"""
