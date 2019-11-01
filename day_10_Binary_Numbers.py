#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    list_bin = list(map(int, bin(n)[2:]))
    result = 0
    maximum = 0

    for item in list_bin:
        if item == 1:
            result += 1
            if result > maximum:
                maximum = result
        else:
            result = 0
    
    print(maximum)
