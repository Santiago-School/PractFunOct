print("Fco. Santiago Carrasco C. 3 ° W 0421")
print(" ")
# practicando funciones 20
def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)  # llama a la función recursivamente
        print(result)  # imprime el resultado acumulado
    else:
        result = 0  # caso base, cuando k es 0
    return result  # devuelve el resultado

print("\n\nrecursion example results")  # mensaje antes de imprimir resultados
tri_recursion(6)  # llama a la función de recursión con 6
