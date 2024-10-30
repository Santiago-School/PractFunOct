print("Fco. Santiago Carrasco C. 3 ° W 0421")
print(" ")
# practicando funciones 8
def myfunction(**niño):
    print("El apellido paterno es:  " + niño["lname"])  # imprime el apellido del niño
myfunction(fname="Santiago", lname="Carrasco")  # llama a la función con argumentos nombrados
