def chai_flavor(flavor= "Masala"):
    """Return the flavor of chai"""
    return flavor

print(chai_flavor.__doc__) #dunder __doc__ returns the value in """"""
print(chai_flavor.__name__) # retur the name of function
# help(len) # return the details of len 

def generate_bill(chai= 0, samosa=0):
    """calculate the total bill  for chai and samosa 
    :param chai: Number of chai cups (10 rupees each)
    :return: (total amt, thank you message)
    """
    total = chai * 10 + samosa * 15
    return total, "Thank you"

print(generate_bill(1,1))