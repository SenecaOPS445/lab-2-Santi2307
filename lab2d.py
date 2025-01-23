#!/usr/bin/env python3

import sys

# Check if there are exactly 2 additional arguments
if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} name age")
    sys.exit()

# Assigning arguments to variables
name = sys.argv[1]
age = sys.argv[2]

# Outputting the message
print(f"Hi {name}, you are {age} years old.")
