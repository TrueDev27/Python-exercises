"""
    Program to display the following pattern

    example:
        Enter number (n): 4
        pattern:
        4     4
         3   3
          2 2
           1
"""
n = int(input("Enter a number: \n"))
#n = 4
for i in range(1, n + 1) :
    for j in range (2 * n - 1 , i - 1 , -1) :
        if i == j or j == 2*n-i :
            print(n - i + 1, end="")
        else :
            print(" ", end="")
    print()
       
