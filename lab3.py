# define the getValue() module 
def getValue():
    purchaseValue = float(input('Please enter the invoice total: '))
    return purchaseValue

#define the itemValue module
def itemValue():
    itemVal = 0.00
    numItems = int(input('How many items would you like to markdown?'))

    #Run a for loop controled by the input of numItems
    for counter in range(1,numItems + 1):
        cost = float(input('Please enter the items cost: $'))   
        itemVal = itemVal + cost
    return itemVal
# Declare the redeuced by module to calculate the sum in dollars
def redeucedby(x,y):
    sum = int(x - y)
    return sum

# declare the main()

def main():
    shipmentValue = getValue()
    itemCost = itemValue()
    markdownAmount = int(redeucedby(shipmentValue,itemCost))
    print('You spent: $', shipmentValue, '\n You did a total markdown for: $',itemCost)
main()