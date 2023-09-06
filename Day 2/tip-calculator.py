#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

bill = input("Welcome to the tip calculator. \nWhat was the total bill? $")
tip = input("What percentage tip would you like to give? 10, 12 or 15? ")
pax = input("How many people to split the bill? ")
bill_per_pax = (float(bill)/float(pax))*((float(tip)/100)+1)
print("Each person should pay: $%.2f" % bill_per_pax)
