number = int(input("Enter five digits number: "))
fifth_number = number % 10
number = number // 10

fourth_number = number % 10
number = number // 10

third_number = number % 10
number = number // 10

second_number = number % 10
number = number // 10

first_number = number % 10
number = number // 10
print(first_number,  second_number,   third_number,   fourth_number,   fifth_number,   )
