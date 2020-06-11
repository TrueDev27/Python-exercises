"""
    Program to display a Pascal's Triange
    input should be number of rows.
    input  = 4 
            1
        1       1
    1       2       1
1       3       3       1

"""
#n = int(input("Enter a number: \n"))
n = 4
#a = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
a = []
for i in range(1, n + 1) :
    a.append([1])
for i in range(len(a)) :
   if i == len(a) :
    a[i].append(1)
   else :
    a[i].append(i+1)


    
print(a)

     
""" for i in range(n):                      # row
    for j in range(n - i, 0, -1):       # col
        print(end=" \t")                # printitng blank + tabs    
    for j in range(i+1):                  # col 
        print(a[i][j] , end="\t\t")
    print() """