print("Fco. Santiago Carrasco C. 3 ° W 0421")
print(" ")
# practicando funciones 20
def trirecursion(k):
    if(k > 0):
        resultado = k + trirecursion(k - 1)  # llama a la función recursivamente
        print(resultado)  # imprime el resultado acumulado
    else:
        resultado = 0  # caso base, cuando k es 0
    return resultado  # devuelve el resultado

print("\n\n ejercios de recursion ")  # mensaje antes de imprimir resultados
trirecursion(6)  # llama a la funcion de recursión con 6
