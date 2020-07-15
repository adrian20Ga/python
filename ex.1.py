
def fib2file(n, fname): #assign the funtion

    #open the doc with "open" and write
    with open(fname, 'w') as of:

        #assign the variables
        f1, f2, f3 = 0, 1, 0
        #use for to count the sequence of fibonacci
        for _ in range(n):
            #below we do the operation of fibonacci
            f1 = f2
            f2 = f3
            f3 = f1 + f2 #end the operation

            #write the document
            of.write('%d\n' % f3)