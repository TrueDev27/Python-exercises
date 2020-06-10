"""
    Program to display the following pattern

    example:
        Enter number of rows(n): 4
        pattern:
        1
        1 2
        1 2 3
        1 2 3 4

"""
n = int(input("Enter a number: \n"))
for i in range(1,n+1) :
    for j in range (1,i+1) :
        print(j, end=" ")
    print()
        
