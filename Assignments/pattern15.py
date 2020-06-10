"""
    Program to display the following pattern

    example:
        Enter number (n): 4
        pattern:
              1
            2 3 2
          3 4 5 4 3
        4 5 6 7 6 5 4
"""

#n = int(input("Enter a number: \n"))
n = 4
for i in range(1, n + 1) :
    for j in range (1,2*n) :
      if i == j + n - 1 or j == 2 * n  :
        print(n, end=" ")
      else :
        print(" ", end="")
    print()