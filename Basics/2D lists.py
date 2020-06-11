a = [[1,2],[3,4]]

""" for i in range(len(a)) :
    print(end="\t")
    for j in range (len(a[i])) :
        print(a[i][j], end=" ")
    print() """

for row in a :
    print(row)
    for col in row :
        print(row, end=" ")
    print() 
