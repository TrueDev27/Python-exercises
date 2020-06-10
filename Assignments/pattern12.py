"""
    Program to display Floyd's Triangle

    example:
        Enter number of rows(n): 4
        pattern:
        1
        2   3
        4   5   6
        7   8   9   10

    Hint: There is a tab after each number in the Floyd's Triangle. to print tab use "\t" similar to "\n" 
"""

n = int(input("Enter a number: \n"))
a=1
for i in range(1,n+1) :
    for j in range (i) :
        print( a , end="\t")
        a += 1
    print()