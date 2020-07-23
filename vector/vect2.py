
import numpy as np
from datetime import datetime


i = 1

while i< 101:
    print(i)
    i += 1

    if i %3==0 and i%5==0:
      print(" fizzbuzz")

    elif i %3==0:
        print("fizz")

    elif i %5==0:
        print(" buzz")

 # vectorize
start_time= datetime.now()
fiz= np. arange(start=1, stop=100)#loop

print (fiz[((fiz%15==0) | (fiz%3==0) & (fiz%5==0))]) #only fizzbuzz print

end_time= datetime.now()
print("Duration: {}".format(end_time-start_time))