# use if within a function

# define the function
def calcTotal(numberItems, unitCost, taxRate):
   if numberItems < 10:
      discountFactor = 1.0
   else: # discount of 10% off for 10 or more items
      discountFactor = .90
   pretaxCost = round(numberItems * unitCost * discountFactor, 2)
   salesTax = round(pretaxCost * taxRate, 2)
   return pretaxCost, salesTax # return 2 results to the caller

# inputs
count = int(input('Enter # of books: '))
cost = float(input('Enter cost per book ($): '))

# call the function, receiving two results, store them to two variables
pretax, tax = calcTotal(count, cost, .075)

# output
print('Pre-tax: $', pretax)
print('Tax:     $', tax)
print('Total:   $', pretax+tax)

# Change the discount % logic as follows
# 3 or less books --> 10% discount
# 4 to 10 books --> 15% discount
# more than 10 books --> 20% discount
