

# Practicando funciones 1
def myfunction():
    print("hello from a function")

myfunction()

# Practicando funciones 2
def myfunction():
    print("hello from a function")

myfunction()

# Practicando funciones 3
def myfunction(fname):
    print(fname + " refsnes")

myfunction("emil")
myfunction("emil")
myfunction("emil")

# Practicando funciones 4
def myfunction(fname, lname):
    print(fname + " " + lname)

myfunction("emil", "refsnes")

# Practicando funciones 5
def myfunction(fname, lname):
    print(fname + " " + lname)

myfunction("emil")

# Practicando funciones 6
def myfunction(*kids):
    print("the youngest child is " + kids[2])

myfunction("emil", "tobias", "linus")

# Practicando funciones 7
def myfunction(child3, child2, child1):
    print("the youngest child is " + child3)

myfunction(child1="emil", child2="tobias", child3="linus")

# Practicando funciones 8
def myfunction(**kid):
    print("his last name is " + kid["lname"])

myfunction(fname="tobias", lname="refsnes")

# Practicando funciones 9
def myfunction(country="sweden"):
    print("i am from " + country)

myfunction("india")
myfunction()
myfunction("brazil")

# Practicando funciones 10
def myfunction(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]
myfunction(fruits)

# Practicando funciones 11
def myfunction(x):
    return x + 1

print(myfunction(3))
print(myfunction(5))
print(myfunction(9))

# Practicando funciones 12
def myfunction():
    pass

# Practicando funciones 13
def myfunction(x, /):
    print(x)

myfunction(3)

# Practicando funciones 14
def myfunction(x):
    print(x)

myfunction(x=3)

# Practicando funciones 15
def myfunction(x, /):
    print(x)

# myfunction(x=3)  # Esto causaría un error

# Practicando funciones 16
def myfunction(*, x):
    print(x)

myfunction(x=3)

# Practicando funciones 17
def myfunction(x):
    print(x)

myfunction(3)

# Practicando funciones 18
def myfunction(*, x):
    print(x)

# myfunction(3)  # Esto causaría un error

# Practicando funciones 19
def myfunction(a, b, /, *, c, d):
    print(a + b + c + d)

myfunction(5, 6, c=7, d=8)

# Practicando funciones 20
def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("\n\nrecursion example results")
tri_recursion(6)
