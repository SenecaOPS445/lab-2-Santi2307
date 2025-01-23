#!/usr/bin/env python3
# Author: Santiago Delgado
# Author ID: sdelgado
# Date Created: 2025/01/22

import sys

# Assign the first command-line argument to `timer` after converting it to an integer
timer = int(sys.argv[1])

# Countdown loop
while timer > 0:
    print(timer)
    timer -= 1

print("blast off!")
