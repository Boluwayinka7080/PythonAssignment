total_bill = float(input("What is your total bill: "))
membership = bool(input("Yes / No: "))
if(total_bill >= 1000 and membership == Yes):
    print("You have 10% off discount")
if(total_bill >= 1000 and membership == No):
    print("You have 5% off discount")
else:
    print("No discount, your final amount is " + str(total_bill))
