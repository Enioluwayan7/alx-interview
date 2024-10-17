#!/usr/bin/python3
"""
This script calculates the minimum number of operations needed to achieve
exactly n 'H' characters in a text file, starting with a single 'H' character.
Operations allowed are "Copy All" and "Paste".
"""

def minOperations(n):
    """
    Calculate the minimum number of operations needed to get exactly n 'H' characters.
    
    Args:
        n (int): The target number of 'H' characters.
    
    Returns:
        int: The minimum number of operations required to achieve n characters,
             or 0 if n cannot be achieved.
    """
    if n <= 1:
        return 0
    
    operations = 0
    divisor = 2
    
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1
    
    return operations
