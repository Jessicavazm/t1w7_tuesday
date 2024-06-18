# Greeting someone
def greet():
    print("Hello Coder, Max!!")

greet()


# Generalised coding
def greet(name): # <-- This is a parameter
    print(f"Hello Coder, {name}")

greet("Jess") #<-- This is an argument

# Function with two parameters

def greeting(fname, lname):
    print(f"Hello Coder, {fname} {lname}")

greeting("Jessica", "Vaz")   

# Positional arguments
def subtract(a, b): 
    difference = a - b
    return difference
result = subtract(3, 4)
print(result)

# Default argument/ optional parameters
def subtracts(a, b=1): 
    difference = a - b
    return difference
result = subtracts(3)
print(result)

# Keyword argument, you can swap positions since they are defined.

def subtractss(a, b=1): 
    difference = a - b
    return difference
result = subtractss(b=3, a=4)
print(result)