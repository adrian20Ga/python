def primo(num_1): #define a funtion
    for i in range(2, num_1): #a loop for number
        if num_1 % i == 0: #operation
            return False
    return True #a normal return

numero = int(input("Número: ")) #input the number
if primo(numero): #conditional statement
    print("is prime")
else:
    print("not prime") #print the messages