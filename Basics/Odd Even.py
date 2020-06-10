
a=int(input("Enter a number:\n"))
print("Here are the even numbers between 1 to " + str(a) + ":\n")
for i in range (1, a+1):
    if i % 2 == 0:
        print(i, end=" ")
print("\n Here are the odd numbers between 1 to " + str(a) + ":\n")
for i in range (1, a):
    if not i % 2 == 0:
        print(i, end=" ")

