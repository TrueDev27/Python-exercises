"""
    Program to display the following pattern

    example:
        Enter number of rows(n): 4
        pattern:
        4 4 4 4
        3 3 3 
        2 2 
        1

"""
n = int(input("Enter a number: \n"))
for i in range(n+1) :
    for j in range (n, i ,-1) :
        print(n-i, end=" ")
    print()
       