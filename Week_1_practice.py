import random
def genEven():
    '''
    Returns a random even number x, where 0 <= x < 100
    '''
    return random.randrange(0,100,2)
###########################    
def deterministicNumber():
    return 10 # or 12 or 14 or 16 or 18 or 20
###########################
def stochasticNumber():
    '''
    Stochastically generates and returns a uniformly distributed even number between 9 and 21
    '''
    return random.randrange(10,22,2)
###########################    

############################

