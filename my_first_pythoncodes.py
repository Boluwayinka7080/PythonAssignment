#print("Print Horizontally 2" , end= '====')
#print("Print Horizontally 3" , end= '====')
#print("print Horizontally 4" , end= '====')

number = 36

name = "Bolu"

amount =  90.56

is_tall = True

print('=' * 25)
print(number** 0.5)
print ("=" * 25)


print("This is ade's bike")
print('This is ope\'s bike')
print("The hot tea \\ bread")



my_code_doc = """
    The code is meant to collect user name and their age and print it out one after the other 

    """
      
print(my_code_doc)


#Collecting input from terminal



age = int(input("Enter user input: "))

if age > 25:
      print("You are allowed to vote in the Election")

elif age < 25 and age > 18:
    print("You can only have a voters card but cannot vote yet")

elif age < 18 and age > 12:
    print("You are unable to vote")

