#!/usr/bin/env python3
# Author: Santiago Delgado
# Author ID: sdelgado
# Date Created: 2025/01/22

import sys

# Check if a command-line argument is provided
if len(sys.argv) > 1:
    timer = int(sys.argv[1])  # Use the argument as the timer
else:
    timer = 3  # Default timer value if no argument is provided

# Countdown using a while loop
while timer > 0:
    print(timer)
    timer -= 1

# Print "blast off!" after the countdown
print("blast off!")

