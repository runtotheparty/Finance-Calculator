#start
import math

# create two finance calculators - investment and home loan repayment

# ask user to choose which calculation they want to do 'investment' or 'bond' and define each to user
invest_or_bond = input("""Choose either 'Investment' or 'Bond' from the menu below to proceed:
 Investment - to calculate the amount of interest you'll earn on your investment
 Bond - to calculate the amount you'll have to pay on a home loan
: """)


# create error handling - all caps and no caps should be fine, but invalid entries must return error
# use upper and lower to support any input the user might have -
# I found that .casefold works better https://discord.com/channels/1034069063888015380/1037613728662827039/1038843507361710090

# if investment: ask amount of deposit, interest rate as as float, number of years they plan on investing, ask user to input simple or compound interest
if invest_or_bond.casefold() == "investment":
    deposit = round(float(input("Please enter amount of deposit: ")), 2)
    interest_rate = round(float(input("Please enter rate of interest in digits only: ")), 2)
    interest_rate = interest_rate/100
    years = int(input("How many years are you investing for? "))
    interest = input("Simple or Compound interest? ")

    if interest.casefold() == "simple":
        simp_invest_total = round(deposit*(1+interest_rate*years), 2)
        print(f"Your expected total after {years} is £{simp_invest_total}")
        exit()
    
    elif interest.casefold() == "compound":
        comp_invest_total = round((deposit* math.pow((1+interest_rate), years)), 2)
        print (f"Your expected total after {years} years is: £{comp_invest_total}")
        exit()

    # error handling here:    
    else:
        print("Incorrect input. Please enter 'simple' or 'compound'")
        exit ()
   
# If bond: ask value of house, interest rate, number of months to repay and calcuate how much money they have to pay each month
if invest_or_bond.casefold() == "bond":
    house = float(input("Please enter the value of your house: "))
    repay_time = int(input("Please enter how many months your loan is for: "))
    bond_rate = float(input("Please enter your annual interest rate: "))
    bond_rate = (bond_rate/100) / 12
    bond_output = round((bond_rate*house)/(1 - (1+bond_rate)**(-repay_time)), 2)
    print(f"Your monthly repayments will be £{bond_output} per month.")
    exit()

    
# Else return incorrect input
else:
    print("Please enter 'investment' or 'bond'")
    exit()

# I added exits at the end of each if statment as it was incorrectly printing the else "Please enter 'investment' or 'bond'" after successful running
#end