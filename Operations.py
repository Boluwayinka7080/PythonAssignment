first_number = int(input("Enter First Number: "))
second_number = int(input("Enter Second Number: "))
third_number= int(input("Enter Third Number: "))

sum = first_number + second_number + third_number
print("The sum total is " + str(sum))
average = (first_number + second_number + third_number)/3
print("The average of the three numbers is " + str(average))
product = first_number * second_number * third_number
print("The product of the three numbers is " + str(product))

if(first_number > second_number and first_number > third_number):
    print("The largest number is " + str(first_number))
if(second_number > first_number and second_number > third_number):
    print("The largest number is " + str(second_number))
if(third_number > first_number and third_number > second_number):
    print("The largest number is " + str(third_number))

if(first_number < second_number and first_number < third_number):
    print("The smallest number is " + str(first_number))
if(second_number < first_number and second_number < third_number):
    print("The smallest number is " + str(second_number))
if(third_number < first_number and third_number < second_number):
    print("The smallest number is " + str(third_number))

