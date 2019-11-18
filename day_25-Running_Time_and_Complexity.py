# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import sqrt

if __name__ == "__main__":
    def isPrime(n):
        for i in range(2, int(sqrt(n)+1)):
            if n%i == 0:
                return False
        return True

    t = int(input())
    for _ in range(t):
        n = int(input())
        if n >= 2 and isPrime(n):
            print("Prime")
        else:
            print("Not prime")
