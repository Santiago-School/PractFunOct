print("Fco. Santiago Carrasco C. 3 ° W 0421")
print(" ")
# practicando funciones 19
def myfunction(a, b, /, *, c, d):
    print(a + b + c + d)  # imprime la suma de a, b, c y d
myfunction(5, 6, c=7, d=8)  # llama a la función con a, b, c y d
