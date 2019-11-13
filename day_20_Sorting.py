#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
numSwaps = 0
for i in range(n):
    for j in range(n-1):
        if(a[j] > a[j+1]):
            numSwaps+=1
            a[j], a[j+1] = a[j+1], a[j]
    if(numSwaps is 0):
        break
print("Array is sorted in {} swaps.".format(numSwaps))
print("First Element: {}".format(a[0]))
print("Last Element: {}".format(a[-1]))
