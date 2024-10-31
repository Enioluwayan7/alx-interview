#!/usr/bin/python3
"""
A method to check if a given dataset represents valid UTF-8 encoding.
"""

def validUTF8(data):
    """
    Checks if a list of integers represents a valid UTF-8 encoding.

    Parameters:
    data (list): List of integers where each integer represents a byte (1 byte = 8 bits).

    Returns:
    bool: True if data is a valid UTF-8 encoding, else False.
    """
    num_bytes = 0
    first_byte_mask = 1 << 7
    second_byte_mask = 1 << 6

    for num in data:
        byte = num & 0xFF

        if num_bytes == 0:
            if (byte & first_byte_mask) == 0:
                continue
            elif (byte & (first_byte_mask | second_byte_mask)) == first_byte_mask:
                return False
            elif (byte & 0xF0) == 0xE0:
                num_bytes = 3
            elif (byte & 0xE0) == 0xC0:
                num_bytes = 2
            elif (byte & 0xF8) == 0xF0:
                num_bytes = 4
            else:
                return False
        else:
            if (byte & (first_byte_mask | second_byte_mask)) != second_byte_mask:
                return False

        num_bytes -= 1

    return num_bytes == 0
