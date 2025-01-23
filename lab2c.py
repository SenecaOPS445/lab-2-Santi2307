#!/usr/bin/env python3

import sys

# Check for sufficient arguments
if len(sys.argv) < 3:
    print("Error: You must provide a name and an age as arguments.")
    sys.exit(1)

# Assign arguments
name = sys.argv[1]
age = int(sys.argv[2])

# Print the output
print(f"Hi {name}, you are {age} years old.")
