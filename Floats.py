number_one = float(input("Enter first number: "))
number_two = float(input("Enter second number: "))
number_three =float(input("Enter third number: "))

if(number_one > number_two and number_one > number_three):
    print("The highest number is " + str(number_one) )

if(number_two > number_one and number_two > number_three):
    print("The highest number is " + str(number_two))

if(number_three > number_one and number_three > number_two):
    print("The highest number is " + str(number_three))

if(number_one < number_two and number_one < number_three):
    print("The lowest number is " + str(number_one) )

if(number_two < number_one and number_two < number_three):
    print("The lowest number is " + str(number_two))

if(number_three < number_one and number_three < number_two):
    print("The lowest number is " + str(number_three))

if(number_two > number_one and number_three > number_one):
    print("The medium number is " + str(number_two))

if(number_one < number_two and number_three < number_two):
    print("The medium number is " + str(number_three))

if(number_one > number_two and number_two > number_three):
    print("The medium number is " + str(number_two))

    
