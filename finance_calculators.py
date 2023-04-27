import math

# discription of functions available to the user
inv = ("Investment - this option will calculate the amount of interest you'll earn on your investment")
bond = ("Bond - this option will calculate the amount you'll have to repay monthly on a home loan")
print(inv)
print(bond)

# Path choice
investment_or_bond = str(input("Please enter either 'Investment' or 'Bond' to proceed: ")).lower()
if (investment_or_bond == "investment"):
    print("You have chosen the Investment option, please enter the required details")
    deposit = int(input("Please enter the ammount you are depositing in pounds: £"))
    print(deposit)
    interest_rate = float(input("Please enter the required interest rate as a percentage: "))
    print(interest_rate)
    investment_time = int(input("Please enter the number of years you plan on investing: "))
    print(investment_time)
    interest_percentage = (interest_rate/100)
    # Interest Calculations
    simple_interest = int(deposit*(1 + interest_percentage*investment_time))
    compound_interest = int(deposit * math.pow((1+interest_percentage), investment_time))
    # Interest Type
    interest_type = str(input("Would you like to view 'simple' or 'compound' interest? ")).lower()
    if interest_type == "simple":
        print("The total amount once the interest has been applied is " + "£", (simple_interest))
    elif interest_type == "compound":
        print("The total amount once the interest has been applied is " + "£", (compound_interest))
    else:
        print("Please choose one of the options to proceed")
# Bond Path
elif (investment_or_bond == "bond"):
    print("You have chosen the Bond option, please enter the required information to proceed")
    house_value = int(input("Please enter the present value of the house in pounds: "))
    print(house_value)
    interest_rate = float(input("Please enter the required interest rate as a percentage: "))
    print(interest_rate)
    time_to_repay = int(input("Please enter the number of months you plan to take to repay the bond: "))
    print(time_to_repay)
    interest_percentage = (interest_rate/100)
    monthly_interest = (interest_percentage/12)
    # Repayment Formula
    repayment = int((monthly_interest * house_value)/(1 - (1 + monthly_interest)**(- time_to_repay)))
    print("The ammount of money you will have to repay each month is " + "£", (repayment))
else:
    print("Please choose one of the options to proceed")
