def validUTF8(data):
    # Number of bytes in the current UTF-8 character
    num_bytes = 0
    
    # Masks to check the number of leading 1's in a byte
    first_byte_mask = 1 << 7
    second_byte_mask = 1 << 6
    
    # Iterate over each integer in the data list
    for num in data:
        # Check only the 8 least significant bits of each integer
        byte = num & 0xFF
        
        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            if (byte & first_byte_mask) == 0:
                # 1-byte character (0xxxxxxx)
                continue
            elif (byte & (first_byte_mask | second_byte_mask)) == first_byte_mask:
                # Invalid leading byte (10xxxxxx)
                return False
            elif (byte & 0xF0) == 0xE0:
                num_bytes = 3  # 3-byte character
            elif (byte & 0xE0) == 0xC0:
                num_bytes = 2  # 2-byte character
            elif (byte & 0xF8) == 0xF0:
                num_bytes = 4  # 4-byte character
            else:
                return False
        else:
            # Check for a continuation byte (10xxxxxx)
            if (byte & (first_byte_mask | second_byte_mask)) != second_byte_mask:
                return False
            
        # Decrement the bytes remaining in the current character
        num_bytes -= 1
    
    # If we finished with no remaining bytes, the encoding is valid
    return num_bytes == 0
