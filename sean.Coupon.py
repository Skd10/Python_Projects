groceries = int(input("How much did you spend total? $"))

if groceries < 10:
    coupon = "No Coupon!!!"
    print ("You are too cheap!", coupon)

if 10 <= groceries <= 59:
    coupon = groceries * 0.10
    print ("You helped us get rich. You win a coupon worth %.2f"
           %coupon, "which is 10% off!")

if 60 <= groceries <= 99:
    coupon = groceries * 0.20
    print ("You are our slaves now. You paid about 100 bucks. "
             "You win a coupon worth %.2f" %coupon, "which is 20% off!")
    
if 100 <= groceries <= 249:
    coupon = groceries * 0.30
    print ("You must be the fattest person in the world if you bought that much.You win a coupon worth %.2f" %coupon, "which is 30% off!")

    
if groceries >= 250:
    coupon = groceries * 0.40
    print ("You are too wealthy! WHY DID YOU BUY OUR WHOLE STORE!!!"
          "Your coupon is worth" , coupon)
