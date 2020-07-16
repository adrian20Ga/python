
def factorial(numero): #funtion that calculate the factorial
    f = 1
    if numero != 0: #if not equal
        for i in range(1, numero + 1): #loop
            f = f * i #operation
    return f



cantidad = 0
num = int(input("insert a number sir): ")) #input the number
while num != -1: #a great while
    print("Factorial:", factorial(num)) #factorial with the funtion defined
    cantidad += 1
    num = int(input("insert a number sir: ")) # try again sir
