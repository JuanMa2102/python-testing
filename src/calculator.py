def sum(a, b):
    """
    >>> sum(5,7)
    12
    
    >>> sum(1,2)
    3
    
    >>> sum(1,-1)
    0
    """
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
        
        return a * b

def divide(a, b):
    """
    >>> divide(1, 0)
    Traceback (most recent call last):
    ...
    ZeroDivisionError
    """
    if b == 0:
        raise ZeroDivisionError
    return a / b