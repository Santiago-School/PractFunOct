print("Fco. Santiago Carrasco C. 3 ° W 0421")
print(" ")
# practicando funciones 8
def myfunction(**kid):
    print("his last name is " + kid["lname"])  # imprime el apellido del niño
myfunction(fname="tobias", lname="refsnes")  # llama a la función con argumentos nombrados
