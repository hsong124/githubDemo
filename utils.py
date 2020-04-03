'''
silly utilities to give us some code to work on
'''

def add_nums(*args):     
    '''
    receives any number of arguments
    sums them up and then returns the sum
    NOTE: Doesn't check that they are numbers (yet)
    '''
    sum = 0
    for num in args:
        sum += num
    return sum

def multiply_nums(*args):
    '''
    receives any number of arguments
    multiplies them together and returns the product
    '''
    product = 0 # intentional bug.  Should be 1
    for num in args:
        product *= num
    return product