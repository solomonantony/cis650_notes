# 3 functions plus main() (function calling other functions)

# prompt user for inputs
def getSalesInfo():
    count = int(input('Enter # of books: '))
    cost = float(input('Enter cost per book ($): '))
    return count, cost

# calculate the pre-tax cost and tax
def calcTotal(numberItems, unitCost, taxRate):
    pretaxCost = round(numberItems * unitCost, 2)
    salesTax = round(pretaxCost * taxRate, 2)
    return pretaxCost, salesTax

def displaySales(pretax, tax):
   print('Pre-tax:', pretax) #no formatting
   print(f'Pre-tax: {pretax}') #using the f formatter
   print(f'{"Pre-tax":_<10} ${pretax:.2f}') #using left alignment within 10 spaces and 2 decimals
   print(f'{"Pre-tax":_<10} ${pretax:_>6.2f}') #left aligning string within 10 spaces, right aligning 2 decimals within 6 spaces
   print('Tax:     $', tax) #Modify this line using similar format as the previous line
   print('Total:   $', pretax+tax) #Modify this line using similar format as the previous line

# call each function for input, processing, and output
def main():
   count, cost = getSalesInfo()
   pretax, tax = calcTotal(count, cost, .075)
   displaySales(pretax, tax)

main()
#Run the script to see it work.
# Modify lines 20 and 21
