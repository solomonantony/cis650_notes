price = int(input("What is the price of a cup of coffee? "))
cups = int(input("How many cups do you want? "))
total = price * cups
#print("Your total is $" + total + " for " + cups + " cups.")
print(f'Your total is $ {total:.4f} for {cups}.')
