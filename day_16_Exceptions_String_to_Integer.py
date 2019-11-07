#!/bin/python3
import sys

import sys

S = input().strip()

try: 
    print(int(S))
except ValueError: 
    print("Bad String")
