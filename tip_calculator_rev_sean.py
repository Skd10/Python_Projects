#Tip Calculator
#Calculates the total of meal with tip

meal1 = float(input('How much did your meal cost?: '))
meal2 = float(input('How much did this meal cost?: '))

tip_input = int(input('How much would you like your tip to be?: '))

tip_input = tip_input/100

subTotal = meal1 + meal2

tax = subTotal * 0.08

tip = subTotal * tip_input

total = round(tip + tax + subTotal,2)

print ('Your total is $',total,'.' )
