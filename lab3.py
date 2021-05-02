# define the getValue() module 
def getValue():
    shipment_value = float(input('Please enter the invoice total: '))
    return shipment_value

#define the itemValue module
def itemValue():
    numItems = int(input('How many items would you like to markdown?'))

    #Run a for loop controled by the input of numItems
    for counter in range(1,numItems + 1):
        cost = float(input('Please enter the items cost \t : $'))   
        itemVal = cost
        #declare an accumulator variable to hold the running total
        # we can return the running total
        runningTotal = itemVal
        print('Item: ' +str(counter) + '\t' 'Value: ' + str(itemVal))
    print('your running total is ', runningTotal)

getValue()
itemValue()