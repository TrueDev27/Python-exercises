a = input("please enter a number for pattern \n")

#if not int(a):
a=int(a)
#normal
for i in range (1,a+1):
    print("#"*i)

#reverse
for i in range (1, a + 1):
    x = a - i
    print(" " * x, end="")
    print("#" * i)

for i in range (1, a + 1):
    print(" " * (a - i) + "#" * i + " " + "#" * i)    
#else:
#    print("Please enter a number only")


a = input("please enter a number for pattern \n")
a=int(a) 
for i in range (1, a + 1):
    print(" " * (a - i) + "#" * i + " " + "#" * i)
