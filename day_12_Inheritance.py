class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    
    def __init__(self, firstName, lastName, idNum, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNum = idNum
        self.scores = scores
        self.total = 0
        self._get_total(scores)
    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def _get_total(self, scores):
        for score in scores:
            self.total += score
        self.total = self.total/len(scores)

    def calculate(self):
        if self.total < 40:
            return "T"
        elif self.total >= 40 and self.total < 55:
            return "D"
        elif self.total >= 55 and self.total < 70:
            return "P"
        elif self.total >= 70 and self.total < 80:
            return "A"
        elif self.total >= 80 and self.total < 90:
            return "E"
        else:
            return "O"
    

    def printPerson(self):
        person = Person(self.firstName, self.lastName, self.idNum)
        person.printPerson()
        


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
