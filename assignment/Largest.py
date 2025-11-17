a = int(input("Enter first number of choice:  "))
b = int(input("Enter second number of choice: "))
c = int(input("Enter third number of choice: "))

largest_integer = a

if ( b > largest_integer):
   largest_integer = b
if (c > largest_integer):
 largest_integer = c

print("The largest number is " + str(largest_integer))
