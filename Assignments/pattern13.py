"""
    Program to display the following pattern

    example:
        Enter number of rows(n): 4
        pattern:
        1
        01
        101
        0101

"""
#n = int(input("Enter a number: \n"))
n=4
a=1
for i in range(n + 1) :
    if i % 2 == 0 :
       a = 0
    else :
        a = 1     
    for j in range (i) :
        if a == 1 :
            print(a, end="")
            a = 0
        else :
            print(a, end="")
            a = 1
    print()


#other method

num1 = 4
for row in range(num1 + 1):
     for col in range(row):
        #print("[" + str(row) + ", " + str(col) + "]", end=" ")
        if (row+col) % 2 == 0 :
            print(0, end="")
        else :
            print(1, end="")
    print()