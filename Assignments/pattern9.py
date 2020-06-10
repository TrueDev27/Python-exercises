"""

    Program to print first 'n' numbers in a fibonacci series

    example: 
        Enter n: 6
        Fibonacci series is: 0 1 1 2 3 5 
"""
n = int(input("Enter a number: \n"))
a = 0
b = 1
print(a, end=" ")
print(b, end=" ")
for i in range(n-2) :
    c = a + b      
    print(c, end=" ")
    a = b
    b = c    
    
    
