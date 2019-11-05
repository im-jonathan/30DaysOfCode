class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0


    def computeDifference(self):
        total = 0
        for i in self.__elements:
            for j in self.__elements:
                total = abs(i -j)
                if total > self.maximumDifference:
                    self.maximumDifference = total

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
