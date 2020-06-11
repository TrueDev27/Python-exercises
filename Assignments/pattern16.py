"""
    Program to display a Pascal's Triange

    input should be number of rows.
"""
n = int(input("Enter a number: \n"))
#n = 4
for i in range(1, n + 1):           # row
    for j in range(n - i, 0, -1):   # col
        print(end=" \t")            # printing  blank + tab 
    for j in range(1, i + 1):       # col 
      print(i + j - 1, end="\t")    # prining incremental
    for j in range(i - 1, 0 , -1):  # col
      print(j + i - 1, end="\t")    # printing decremental
    print()