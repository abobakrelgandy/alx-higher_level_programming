#!/usr/bin/env python3
def uppercase(str):
    for char in str:
        ascii_val = ord(char)
        if 97 <= ascii_val <= 122:  # ASCII values of 'a' and 'z'
            ascii_val -= 32  # Convert to uppercase
        print("{:c}".format(ascii_val), end="")
    print()
