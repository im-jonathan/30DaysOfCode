# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        even = ""
        odd = ""
        S = input()
        for letter in range(len(S)):
            if letter%2 == 0:
                even += S[letter]
            else:
                odd += S[letter]
        print("{:s} {:s}".format(even, odd))