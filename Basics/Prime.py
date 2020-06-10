
""" a=int(input("Enter a number:\n"))
if (a+2 % 2 and a+2 % 3) == 0:
    print("Not Prime")
else :
    print("Prime") """

a=int(input("Enter a number greater than 2:\n"))
is_prime = True
for i in range(2 , a) :  # runs from 2,3,4.... (n-1)
    if a % i == 0 :
        is_prime = False
        break
if is_prime == True :
    print("Prime")
else :
    print("Not a Prime")