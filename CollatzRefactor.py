import matplotlib.pyplot as plt
import numpy as np

cantidad = 0
num1 = 0
num2 = 0

cantidad = input("How many numbers?: ")
cantidad = int(cantidad)

def askForNumbers(c):
    global arrayq
    arrayq = []
    for i in range(c):
        arrayq.append(int(input("SAY__: ")))
    print(arrayq)

def function(n):
    counter = 0
    array2 = []
    while n != 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n + 1
        counter = counter + 1
        array2.append(n)
    print(array2)
    print("Steps: ",counter)
    return(array2)

askForNumbers(cantidad)

loop = len(arrayq)
if loop > 1:
    while loop > 1:
       for k in arrayq:
          function(k)
          plt.plot(function(k))
          loop = loop - 1
else:
    function(arrayq[0])
    plt.plot(function(arrayq[0]))
    
plt.title("COLLATZ CONJECTURE")
plt.xlabel("Steps")
plt.ylabel("Value")
plt.grid()

plt.show()
