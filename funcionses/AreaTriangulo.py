#Ejemplo para calcular el area del triangulo

#Entradas base
base=int(input("ingrese la base del triangulo:"))
altura=int(input("ingrese la altura del triangulo:"))
#procesp
def calcularAreaTriangulo(b,a):
    area=(b*a)/2
    #print("el area del triangulo es",area)
    return area
resultado=calcularAreaTriangulo(base,altura)
print(f"el area del triangulo es:{resultado}")
