# define the getValue() module 
# Which will get the total of the invoice from the user
def getValue():
    purchaseValue = float(input('Please enter the invoice total: '))
    return purchaseValue

#define the itemValue module
# Using a user controlled for loop and an accumulator we will collect the cost of each item
# and return their total 
def itemValue():
    itemVal = 0.00
    numItems = int(input('How many items would you like to markdown?'))

    #Run a for loop controled by the input of numItems
    for counter in range(1,numItems + 1):
        cost = float(input('Please enter the items cost: $'))   
        itemVal = itemVal + cost
    return itemVal
# Declare the redeuced by module to calculate the sum of the markdowns
def redeucedby(x,y):
    sum = int(x - y)
    return sum

# declare the lossPercent() which will take the shipmentValue and 
# markdownAmount as arguments to conver the loss to a percentage

def lossPercent(a,b):
    perHundred = (b/a) * 100
    return perHundred

# declare the lossAlert()
# Which uses a decision structure to decide which message to output
# which takes markdownPercentage as an argument

def lossAlert(z):
    print(' ')
    if z in range(30,100):
        print('High losses reported, please review order flow ')
    else:
        print('Low losses reported. Please track sales on items ')
        print('to determine if you should keep them on hand ')
    return z


# declare the main()

def main():
    shipmentValue = getValue()
    itemCost = itemValue()
    markdownAmount = int(redeucedby(shipmentValue,itemCost))
    markdownPercentage = lossPercent(shipmentValue,markdownAmount)
    message = lossAlert(markdownPercentage)
    print(' ')
    print('You spent: $', shipmentValue)
    print('You did a total markdown for: $',itemCost)
    print('Which is:',int(markdownPercentage),'%')
main()