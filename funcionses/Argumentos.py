#EJEMPLO DE ARGUMENTOS PREDETERMINADOS

def my_fuction(country = "colombia"):
    print("i am forim "+country)

#invocar la funcion
my_fuction("sweden")
my_fuction("india")
my_fuction()
my_fuction("brazil")

#argumentos arbitriarios
def mostrarEstudiantes(*args):
    print("el estudiante :"+args[2])

mostrarEstudiantes("email","tobias","linus")


#Argumentos de palabras claves

def mostrarCarros(carro1,carro2,carro3):
    print("el carro es:" + carro2)
mostrarCarros(carro1="BMW",carro3="ferrari",carro2="ford")

def mostrarCliente(**kwargs):
    print("su apellido es "+kwargs["apellido"])
    
mostrarCliente(nombre ="tobias",apellido="refsnes")
