#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    i = 1
    while i <= 10:
        result = n*i
        print("{:d} x {:d} = {:d}".format(n, i, result))
        i += 1