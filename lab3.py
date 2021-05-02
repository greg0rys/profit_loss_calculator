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
    sum = x - y
    return sum

# declare the lossPercent() which will take the shipmentValue and 
# markdownAmount as arguments to conver the loss to a percentage

def lossPercent(a,b):
    # When calculating percent we know the maths is
    # x/y = (y/x) * 100
    # This module will not do the multiplication - it will only do the division
    # as the main module will format this output and the format('%') function will
    # actually perform the multiplication when it formats the floating point number
    perHundred = (b/a)
    return perHundred

# declare the lossAlert()
# Which uses a decision structure to decide which message to output
# which takes markdownPercentage as an argument

def lossAlert(z):
    print(' ')
    if z > 100:
        print('High losses reported, please review order flow ')
    elif z > 30:
        print('Please don\'t order anymore')
    else:
        print(' Low losses reported. \n Please track sales on items ',sep = '')
        print(' to determine if you should keep them on hand ')
    return z


# declare the main()

def main():
    shipmentValue = getValue()
    itemCost = itemValue()
    markdownAmount = redeucedby(shipmentValue,itemCost)
    markdownPercentage = lossPercent(shipmentValue,itemCost)
    message = lossAlert(itemCost)
    print(' ')
    print('You spent: $', format(shipmentValue, ',.2f'),sep='')
    print('You did a total markdown for: $',format(itemCost, ',.2f'), sep='')
    print('Which is: ', format(markdownPercentage, '.1%'), sep='')
main()