import sys

a=int(input("Enter a number greater than 2:\n"))
for i in range(2 , a) :  # runs from 2,3,4.... (n-1)
    if a % i == 0 :
        print("Not a Prime")
        sys.exit()
print("Prime")
