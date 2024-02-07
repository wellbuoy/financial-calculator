#====import math====
import math

print("\nfinancial calculator")

print("\nchose either investment or bond below")

print("\ninvestment - to calculate the amount of interest you'll earn on your investment")

print("\nbond - to calculate the amount you'll have to pay on a home loan")

enter = input("\nEnter investment or bond.").lower()
if enter == "investment":

#if the user selects ‘investment’, ask the user to input the amount of money that they are depositing

    amount = float(input("\nHow much are you depositing?"))

#the interest rate (as a percentage). Only the number of the interest rate should be entered — don’t worry about having to deal with the
#added ‘%’, e.g. The user should enter 8 and not 8%. 
  
    rate = float(input("\nHow much is the rate"))

#the number of years they plan on investing.    

    years = float(input("\nHow many years?"))

#then ask the user to input if they want “simple” or “compound” interest, and store this in a variable called interest. Depending on
#whether or not they typed “simple” or “compound”, output the appropriate amount that they will get back after the given period, at the specified interest rate.

    interest = input("\nPlease enter if you want simple or compound interest. type simple or compound: ").lower()
    if interest == "simple":

#the Python equivalent is very similar: A = P *(1 + r*t) 
       
        answer = round((amount * (1 + rate/100 * years)), 2)
        print(f"\nYour investment will be R{answer} after {years} years.")

#the total amount when compound interest is applied is calculated as :
#the Python equivalent is slightly different: A = P * math.pow((1+r),t)

    elif interest == "compound":
        answer = round(amount * math.pow((1 + rate/100), years), 2)
        print(f"\nYour investment will be R{answer} after {years} years.")
    else:
        print("\nYou have not selected interest correctly.Please try again.")

#If the user selects ‘bond’, ask the user to input the present value of the house. e.g. 100000
#The interest rate. e.g. 7
#The number of months they plan to take to repay the bond. e.g. 120

elif enter == "bond":
    house = float(input("\nPlease enter the present value of the house: "))
    rate = float(input("\nPlease enter the interest rate as a percentage: "))
    months = float(input("\nPlease enter the number of months you plan to repay: "))
    
#Calculate how much money the user will have to repay each month and output the answer.

    answer = round(((rate / 12 / 100 * house) / (1 - math.pow((1 + rate / 12 / 100), -months))), 2)
    print(f"Your monthly bond repayment will be R{answer}.")
else:
    print("You have not entered the calculation correctly.Please try again.")