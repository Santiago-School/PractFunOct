# 1. definicion de una función simple
def mifuncion():
    print("hola desde una funcion")

# 2. llamada a la funcion
mifuncion()

# 3. funcion con un argumento
def mifuncionconnombre(fname):
    print(fname + " refsnes")

mifuncionconnombre("kevin")
mifuncionconnombre("canelitas")
mifuncionconnombre("santiago")

# 4. funcion que espera dos argumentos
def mifunciondosargumentos(fname, lname):
    print(fname + " " + lname)

mifunciondosargumentos("lazo", "cuerda")

# 5. llamada a funcion con menos argumentos
# esto generara un error porque falta el segundo argumento

# 6. funcion con argumentos variables
def mifuncionconkids(*kids):
    print("el hijo menor es " + kids[2])

mifuncionconkids("", "La grandota", "cami")

# 7. argumentos con sintaxis clave=valor
def mifuncionconhijos(child3, child2, child1):
    print("el hijo menor es " + child3)

mifuncionconhijos(child1="cristina", child2="Carlitos", child3="Kevinsito")

# 8. argumentos arbitrarios de palabras clave
def mifuncionconkwargs(**kid):
    print("su apellido es " + kid["lname"])

mifuncionconkwargs(fname="Adrian", lname="Correa")

# 9. valores por defecto en parametros
def mifuncionconpais(pais="Peru York"):
    print("soy de " + pais)

mifuncionconpais("Brazil")
mifuncionconpais()
mifuncionconpais("España")

# 10. pasar una lista como argumento
def mifuncionconlista(comida):
    for x in comida:
        print(x)

frutas = ["piña", "cereza", "Sanida"]
mifuncionconlista(frutas)

# 11. devolver valores desde una funcion
def mifuncionconretorno(x):
    return x + 5

print(mifuncionconretorno(3))
print(mifuncionconretorno(5))
print(mifuncionconretorno(9))

# 12. declaracion pass para funciones vacias
def funcionvacia():
    pass  # funcion sin contenido

# 13. argumentos solo posicionales
def mifuncionposicional(x, /):
    print(x)

mifuncionposicional(3)
# mifuncionposicional(x=3)  # esto generara un error

# argumentos solo de palabra clave
def mifuncionpalabraclave(*, x):
    print(x)

mifuncionpalabraclave(x=3)
# mifuncionpalabraclave(3)  # esto generara un error

# combinar argumentos posicionales y de palabra clave
def mifuncioncombinada(a, b, /, *, c, d):
    print(a + b + c + d)

mifuncioncombinada(5, 6, c=7, d=8)

# 14. recursividad
def sumarecursiva(k):
    if k > 0:
        resultado = k + sumarecursiva(k - 1)
        print(resultado)
    else:
        resultado = 0
    return resultado

print("\nresultados de la suma recursiva:")
sumarecursiva(6)
